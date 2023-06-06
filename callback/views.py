from datetime import datetime
import json
import time
from django.conf import settings
from django.http import HttpResponse
import requests
from callback.forms import CallbackForm
from common.loggers import logger
from django.template.loader import render_to_string
from django.core.mail import send_mail


def callback_form(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'POST':
        # time.sleep(3)
        form = CallbackForm(request.POST)
        if form.is_valid():
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

                except Exception as e:
                    logger.error(e)
                
                # msg = 'Ваш запрос был успешно отправлен. Спасибо!'
                # logger.info(msg)
                # return HttpResponse(msg, status=200)
                msg = {
                    'status': 'ok', 
                    'message': 'Ваш запрос был успешно отправлен. Спасибо!'
                }
                logger.info(msg)
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
    


# def callback_form(request):
#     if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'POST':
#         # time.sleep(3)
#         form = CallbackForm(request.POST)
#         # data = {'message': 'not ok'}
#         if form.is_valid():
#             # if result['success'] == True and result['score'] >= 0.5:
#             recaptcha_response = request.POST.get('recaptcha')
#             data = {
#                 'secret': settings.RECAPTCHA_PRIVATE_KEY,
#                 'response': recaptcha_response
#             }
#             r = requests.post(
#                 'https://www.google.com/recaptcha/api/siteverify', data=data)
#             result = r.json()

#             print(result)

#             # ''' if reCAPTCHA returns True '''
#             # if result['success']:
#             #     ''' Send email '''
#             #     subject = "Website Inquiry"
#             #     body = {
#             #     'first_name': form.cleaned_data['first_name'],
#             #     'last_name': form.cleaned_data['last_name'],
#             #     'email': form.cleaned_data['email_address'],
#             #     }
#             #     message = "\n".join(body.values())

#             #     try:
#             #     send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
#             #     except BadHeaderError:
#             #     return HttpResponse('Invalid header found.')
#             #     messages.success(request, "Message sent." )
#             #     return redirect ("main:homepage")

#             # ''' if reCAPTCHA returns False '''
#             # messages.error(request, 'Invalid reCAPTCHA. Please try again.')

#             # captcha_score = form.cleaned_data['captcha'].get('score')

#             subject = 'Обратный звонок'
#             name = form.cleaned_data.get('name')
#             phone = form.cleaned_data.get('phone')

#             context = {
#                 'subject': subject, 
#                 'name': name,
#                 'phone': phone, 
#                 'date': datetime.now()
#             }

#             html_body = render_to_string(
#                 'email/callback.html', context
#             )
#             text_body = render_to_string(
#                 'email/callback.txt', context
#             )

#             print(html_body)

#             # try:
#             # email = EmailMessage(
#             #     title,
#             #     html,
#             #     settings.EMAIL_HOST_USER,  # from address
#             #     settings.LIST_OF_EMAIL_RECIPIENTS, # recipients
#             #     reply_to=[]  # reply to address set by your user
#             # )
#             # email.send()

#             # send_mail(
#             #     title,
#             #     plain,
#             #     'some@sender.com',
#             #     ['some@receiver.com'],
#             #     html_message=html,
#             # )

#             # message = EmailMultiAlternatives(
#             #     subject=title,
#             #     body="mail testing",
#             #     from_email=settings.EMAIL_HOST_USER,
#             #     reply_to=[]
#             # )
#             # message.attach_alternative(html_body, "text/html")
#             # message.send(fail_silently=False)

#             send_mail(
#                 subject,
#                 message=text_body,
#                 html_message=html_body,
#                 recipient_list=settings.LIST_OF_EMAIL_RECIPIENTS,
#                 from_email=settings.EMAIL_HOST_USER,
#                 fail_silently=False,
#             )

#             # except Exception as e:
#             #     # logger.error(e)
#             #     print(e)

#             return HttpResponse(status=200)
#         else:
#             # return HttpResponse({'message': form.errors.as_data()}, status=200)
#             return HttpResponse(json.dumps(form.errors.as_json(), cls=DjangoJSONEncoder), status=200)
#     else:
#         return HttpResponse(status=405)



# @receiver(user_signed_up, sender=User)
# def send_to_email_user_signed_up(sender, **kwargs):
#     logger = logging.getLogger('send_to_admin')
#     logger.info(_('User %(user)s signed up') %
#                 {'user': kwargs['user'].username})
