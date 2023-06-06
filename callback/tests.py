import os
import json
from django.test import TestCase, Client
from django.urls import reverse
from callback.forms import CallbackForm

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