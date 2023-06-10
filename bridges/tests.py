from django.test import TestCase, Client
from django.urls import reverse
from bridges.models import Bridge


class BridgeTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test bridge detail view """

        obj = Bridge.objects \
        .prefetch_related('hwaw') \
        .prefetch_related('portfolio_images') \
        .prefetch_related('portfolio_videos') \
        .get()

        response = self.client.get(reverse(obj.slug))
        self.assertEqual(response.status_code, 200)

    def test_detail_not_exists(self):
        """ Test bridge detail view not exists """

        self.assertRaises(Bridge.DoesNotExist, Bridge.objects.get, slug='anything')
