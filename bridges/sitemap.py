from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class BridgeSitemap(Sitemap):

    def items(self):
        return ['bridges']
    
    def lastmod(self, obj):
        return obj.updated_at

    def location(self, item):
        return reverse(item)
