import os
from django.core.mail import EmailMessage
from django.test import TestCase, Client
from django.core import mail
from django.urls import reverse
from django.utils.translation import activate
from feedback.forms import FeedbackForm


class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        # mail.send_mail(
        #     'Subject here',
        #     'Here is the message.',
        #     'from@example.com', ['to@example.com'],
        #     fail_silently=False
        # )
        email = EmailMessage(
            'Subject here',
            'Here is the message.',
            'from@example.com', # from address
            ['to@example.com'], # recipients
            reply_to=['other@example.com',]  # reply to address set by your user
        )
        email.send()
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')


class FeedbackFormTest(TestCase):
    def setUp(self):
        os.environ['RECAPTCHA_DISABLE'] = 'True'

    def tearDown(self):
        if 'RECAPTCHA_DISABLE' in os.environ.keys():
            del os.environ['RECAPTCHA_DISABLE']

    def test_empty_fields(self):
        form_data = {
             'sender': '',
             'subject': '',
             'message': '',
             'recaptcha_response_field': 'PASSED',
        }
        form = FeedbackForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_email_is_invalid(self):
        form_data = {
             'sender': 'foo@bar',
             'subject': 'test feedback',
             'message': 'TEST test TeSt tEsT',
             'recaptcha_response_field': 'PASSED',
        }
        form = FeedbackForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_email_is_valid(self):
        form_data = {
             'sender': 'foo@bar.baz',
             'subject': 'test feedback',
             'message': 'TEST test TeSt tEsT',
             'recaptcha_response_field': 'PASSED',
        }
        form = FeedbackForm(data=form_data)
        self.assert_(form.is_valid())


class FeedbackPageTest(TestCase):
    def setUp(self):
        os.environ['RECAPTCHA_DISABLE'] = 'True'
        self.client = Client()

        self.form_data = {
            'sender': 'foo@bar.baz',
            'subject': 'test feedback',
            'message': 'TEST test TeSt tEsT',
            'recaptcha_response_field': 'PASSED',
        }

    def tearDown(self):
        if 'RECAPTCHA_DISABLE' in os.environ.keys():
            del os.environ['RECAPTCHA_DISABLE']

    def test_feedback_get(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/en/feedback/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/ru/feedback/')
        self.assertEqual(response.status_code, 404)

    def test_feedback_post(self):
        response = self.client.post(
            reverse('feedback:form'),
            self.form_data
        )
        self.assertRedirects(response, expected_url=reverse('feedback:success'), status_code=302, target_status_code=200)

        activate('en')
        self.form_data.update({
            'sender': 'foo@bar',
            'subject': '',
            'message': '',
        })
        response = self.client.post(
            reverse('feedback:form'),
            self.form_data
        )
        self.assertEqual(response.status_code, 200)
        # self.assertFormError(response, 'form', 'subject', 'This field is required.')
        # self.assertFormError(response, 'form', 'message', 'This field is required.')
        # self.assertFormError(response, 'form', 'sender', 'Enter a valid email address.')

# class AjaxUserLoggedLikeTest(TestCase):
#
#     fixtures = ['fixtures/db.json',]
#
#     def setUp(self):
#         self.client = Client()
#         self.client.login(username='test', password='test')
#
#     def test_valid_form(self):
#         w = Whatever.objects.create(title='Foo', body='Bar')
#         data = {'title': w.title, 'body': w.body,}
#         form = WhateverForm(data=data)
#         self.assertTrue(form.is_valid())
#
#     def test_invalid_form(self):
#         w = Whatever.objects.create(title='Foo', body='')
#         data = {'title': w.title, 'body': w.body,}
#         form = WhateverForm(data=data)
#         self.assertFalse(form.is_valid())


# class MyTests(TestCase):
#     def test_forms(self):
#         form_data = {'something': 'something'}
#         form = MyForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
# class MyTests(TestCase):
#     def test_forms(self):
#         response = self.client.post("/my/form/", {'something':'something'})
#         self.assertFormError(response, 'form', 'something', 'This field is required.')

# self.assertContains(response, "Invalid message here", 1, 200)


# def test_valid_entry_create(self):
#     self.c.login(username='test', password='test')
#     data = {'text': 'Test text', 'title': 'Test title'}
#     data['user'] = self.user.id
#     self.assertEqual(BlogEntry.objects.count(), 0)
#     response = self.c.post(reverse('entry_create'), data)
#     self.assertEqual(response.status_code, 302)
#     self.assertEqual(BlogEntry.objects.count(), 1)
#
# def test_invalid_entry_create(self):
#     self.c.login(username='test', password='test')
#     data = {'text': 'Test text'}
#     response = self.c.post(reverse('entry_create'), data)
#     self.assertEqual(response.status_code, 200)
#     self.assertFormError(response, "form", "title", "This field is required.")
