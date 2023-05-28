from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from staircases.models import Staircase


class StaircaseSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Staircase.is_visible_objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('staircases:detail', kwargs={'slug': obj.slug})
