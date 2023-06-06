from django.test import TestCase, Client
from django.urls import reverse


class ContactPageTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test contacts detail view """

        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)
