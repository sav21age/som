from django.test import TestCase, Client
from django.urls import reverse
from index.models import Index


class IndexPageTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test index detail view """

        obj = Index.objects \
            .prefetch_related('hwaw') \
            .prefetch_related('block_price') \
            .prefetch_related('block_svg') \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .get()

        response = self.client.get(reverse(obj.slug))
        self.assertEqual(response.status_code, 200)

    def test_detail_not_exists(self):
        """ Test index detail view not exists """

        self.assertRaises(Index.DoesNotExist, Index.objects.get, slug='anything')
