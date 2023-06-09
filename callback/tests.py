import os
import json
from datetime import datetime, timezone
from django.conf import settings
from django.test import TestCase, Client
from django.urls import reverse
from callback.forms import CallbackForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core import mail


class SendMailTest(TestCase):
    def test_send_email_fail(self):
        """ Test send_mail """

        send_mail(
            '',
            message='',
            recipient_list='',
            from_email='',
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 0)

    def test_send_email_ok(self):
        """ Test send_mail """

        subject = 'Обратный звонок'
        name = 'Имя'
        phone = '+77777777777'

        context = {
            'subject': subject,
            'name': name,
            'phone': phone,
            'date': datetime.now(timezone.utc)
        }

        html_body = render_to_string(
            'callback/email/callback.html', 
            context
        )

        text_body = render_to_string(
            'callback/email/callback.txt', 
            context
        )

        send_mail(
            subject,
            message=text_body,
            html_message=html_body,
            recipient_list=settings.LIST_OF_EMAIL_RECIPIENTS,
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Обратный звонок')


class CallbackFormTest(TestCase):
    def setUp(self):
        os.environ['RECAPTCHA_DISABLE'] = 'True'

    def tearDown(self):
        if 'RECAPTCHA_DISABLE' in os.environ.keys():
            del os.environ['RECAPTCHA_DISABLE']

    def test_empty_fields(self):
        """ Test callback form empty """
        form_data = {
            'name': '',
            'phone': '',
            'recaptcha': 'PASSED',
        }
        form = CallbackForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_empty_name(self):
        """ Test callback form empty name """

        form_data = {
            'name': '',
            'phone': '+79215555555',
            'recaptcha': 'PASSED',
        }
        form = CallbackForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_phone_name(self):
        """ Test callback form empty phone """

        form_data = {
            'name': 'Тест',
            'phone': '',
            'recaptcha': 'PASSED',
        }
        form = CallbackForm(data=form_data)
        self.assertFalse(form.is_valid())


    def test_is_valid(self):
        """ Test callback form valid """

        form_data = {
            'name': 'Тест',
            'phone': '+79215555555',
            'recaptcha': 'PASSED',
        }
        form = CallbackForm(data=form_data)
        self.assertTrue(form.is_valid())


class CallbackRequestTest(TestCase):
    def setUp(self):
        self.client = Client()
        os.environ['RECAPTCHA_DISABLE'] = 'True'

    def tearDown(self):
        if 'RECAPTCHA_DISABLE' in os.environ.keys():
            del os.environ['RECAPTCHA_DISABLE']

    def test_form_request_405(self):
        """ Test request 405 """
        response = self.client.post(reverse('callback:request'))
        self.assertEqual(response.status_code, 405)


    def test_form_empty_name(self):
        """ Test request empty name """

        json_data = {
            'name': '',
            'phone': '+79215555555',
            'recaptcha': json.dumps({'score': 0.5, 'success': True}),
        }

        response = self.client.post(
            reverse('callback:request'), 
            json_data, 
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)

        res = json.loads(response.content.decode('utf-8'))
        self.assertEqual(
            res, 
            {
                'status': 'error',
                'message': 'Произошла ошибка. Пожалуйста попробуйте позже.'
            }
        )

    def test_form_empty_phone(self):
        """ Test request empty phone """

        json_data = {
            'name': 'Тест',
            'phone': '',
            'recaptcha': json.dumps({'score': 0.5, 'success': True}),
        }

        response = self.client.post(
            reverse('callback:request'), 
            json_data, 
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)

        res = json.loads(response.content.decode('utf-8'))
        self.assertEqual(
            res, 
            {
                'status': 'error',
                'message': 'Произошла ошибка. Пожалуйста попробуйте позже.'
            }
        )

    def test_form_request_failed(self):
        """ Test request failed """

        json_data = {
            'name': 'Тест',
            'phone': '+79215555555',
            'recaptcha': json.dumps({'score': 0.5, 'success': False}),
        }

        response = self.client.post(
            reverse('callback:request'), 
            json_data, 
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)

        res = json.loads(response.content.decode('utf-8'))
        self.assertEqual(
            res, 
            {
                'status': 'error',
                'message': 'Ошибка reCAPTCHA. Пожалуйста попробуйте позже.',
            }
        )

    def test_form_request_success(self):
        """ Test request sucess """

        json_data = {
            'name': 'Тест',
            'phone': '+79215555555',
            'recaptcha': json.dumps({'score': 0.5, 'success': True}),
        }

        response = self.client.post(
            reverse('callback:request'), 
            json_data, 
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)

        res = json.loads(response.content.decode('utf-8'))
        self.assertEqual(
            res, 
            {
                'status': 'ok',
                'message': 'Ваш запрос был успешно отправлен. Спасибо!', 
            }
        )