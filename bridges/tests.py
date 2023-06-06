from django.test import TestCase, Client
from django.urls import reverse


class BridgeTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test bridge detail view """

        response = self.client.get(reverse('bridges'))
        self.assertEqual(response.status_code, 200)
