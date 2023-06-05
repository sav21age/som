from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from railing.models import Railing


class RailingSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Railing.is_visible_objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('railing:detail', kwargs={'slug': obj.slug})
