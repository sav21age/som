from django.test import TestCase, Client
from django.urls import reverse


class IndexPageTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test index detail view """

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
