from django.test import TestCase, Client
from django.urls import reverse
from terraces.models import Terrace


class TerraceTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test terrace detail view """

        obj = Terrace.objects.get()

        response = self.client.get(reverse(obj.slug))
        self.assertEqual(response.status_code, 200)

    def test_detail_not_exists(self):
        """ Test terrace detail view not exists """

        self.assertRaises(Terrace.DoesNotExist, Terrace.objects.get, slug='anything')
