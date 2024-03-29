from django.test import TestCase, Client
from django.urls import reverse
from staircases.models import Staircase


class StaircasesTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def setUp(self):
        self.client = Client()

    def test_detail(self):
        """ Test staircases detail view """

        obj = Staircase.is_visible_objects \
            .prefetch_related('hwaw') \
            .prefetch_related('block_price') \
            .prefetch_related('block_svg') \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .all()[:1].get()

        response = self.client.get(reverse('staircases:detail', kwargs={'slug': obj.slug}))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('staircases:detail', kwargs={'slug': 'anything'}))
        self.assertEqual(response.status_code, 404)


class StaircaseObjectTest(TestCase):
    fixtures = ['fixtures/db.json', ]

    def test_create_object(self):
        """ Test create staircase object """

        obj = Staircase()
        obj.head_title = 'Заголовок страницы'
        obj.meta_description = 'Описание страницы'
        obj.name = 'h1 заголовок'
        obj.slug = 'slug'
        obj.save()
