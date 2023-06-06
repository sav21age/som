from django.test import TestCase, Client
from django.urls import reverse
from steps.models import Steps


class StepsTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test steps detail view """

        obj = Steps.is_visible_objects \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .all()[:1].get()

        response = self.client.get(reverse('steps:detail', kwargs={'slug': obj.slug}))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('steps:detail', kwargs={'slug': 'anything'}))
        self.assertEqual(response.status_code, 404)
