from django.test import TestCase, Client
from django.urls import reverse
from porch.models import Porch


class PorchTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test porch detail view """

        obj = Porch.is_visible_objects \
            .prefetch_related('hwaw') \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .all()[:1].get()

        response = self.client.get(reverse('porch:detail', kwargs={'slug': obj.slug}))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('porch:detail', kwargs={'slug': 'anything'}))
        self.assertEqual(response.status_code, 404)
