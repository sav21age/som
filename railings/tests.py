from django.test import TestCase, Client
from django.urls import reverse
from railings.models import Railing


class RailingTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test railing detail view """

        obj = Railing.is_visible_objects \
            .prefetch_related('portfolio_images') \
            .all()[:1].get()

        response = self.client.get(reverse('railings:detail', kwargs={'slug': obj.slug}))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('railings:detail', kwargs={'slug': 'anything'}))
        self.assertEqual(response.status_code, 404)
