import json
import os
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse
import requests
from callback.forms import CallbackForm
from common.loggers import logger
from django.template.loader import render_to_string
from django.core.mail import send_mail


def callback_form(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'POST':
        form = CallbackForm(request.POST)
        if form.is_valid():
            score = form.cleaned_data['recaptcha'].get('score')
            print(score)

            if 'RECAPTCHA_DISABLE' in os.environ.keys(): # For tests
                res = json.loads(request.POST.get('recaptcha'))
            else:
                recaptcha_response = request.POST.get('recaptcha')
                data = {
                    'secret': settings.RECAPTCHA_PRIVATE_KEY,
                    'response': recaptcha_response
                }
                req = requests.post(
                    'https://www.google.com/recaptcha/api/siteverify', 
                    data=data
                )

                res = req.json()

            if res['success'] == True and res['score'] >= 0.5:
                subject = 'Обратный звонок'
                name = form.cleaned_data.get('name')
                phone = form.cleaned_data.get('phone')

                context = {
                    'subject': subject,
                    'name': name,
                    'phone': phone,
                    'date': datetime.now()
                }

                html_body = render_to_string(
                    'callback/email/callback.html', 
                    context
                )

                text_body = render_to_string(
                    'callback/email/callback.txt', 
                    context
                )

                try:
                    send_mail(
                        subject,
                        message=text_body,
                        html_message=html_body,
                        recipient_list=settings.LIST_OF_EMAIL_RECIPIENTS,
                        from_email=settings.EMAIL_HOST_USER,
                        fail_silently=False,
                    )

                    # msg = 'Ваш запрос был успешно отправлен. Спасибо!'
                    # logger.info(msg)
                    # return HttpResponse(msg, status=200)
                    msg = {
                        'status': 'ok', 
                        'message': 'Ваш запрос был успешно отправлен. Спасибо!'
                    }
                    logger.info(msg)
                    return HttpResponse(json.dumps(msg))

                except Exception as e:
                    logger.error(e)

                    msg = {
                        'status': 'error',
                        'message': 'Произошла ошибка. Пожалуйста попробуйте позже.'
                    }
                    return HttpResponse(json.dumps(msg))
            else:
                # msg = 'Ошибка reCAPTCHA. Пожалуйста попробуйте позже.'
                # logger.info(msg)
                # return HttpResponse(msg, status=400)
                msg = {
                    'status': 'error',
                    'message': 'Ошибка reCAPTCHA. Пожалуйста попробуйте позже.'
                }
                logger.info(msg)
                return HttpResponse(json.dumps(msg))
        else:
            # msg = 'Произошла ошибка. Пожалуйста попробуйте позже.'
            # logger.info(msg)
            # return HttpResponse(msg, status=400)
            msg = {
                'status': 'error',
                'message': 'Произошла ошибка. Пожалуйста попробуйте позже.'
            }
            logger.info(msg)
            return HttpResponse(json.dumps(msg))
    else:
        return HttpResponse(status=405)  
