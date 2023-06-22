from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from bridges.models import Bridge


class BridgeSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['bridges']
        return Bridge.is_visible_objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at

    # def location(self, item):
        # return reverse(item)

    def location(self, obj):
        return reverse('crossing-bridge')
