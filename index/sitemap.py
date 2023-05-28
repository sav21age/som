from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class IndexSitemap(Sitemap):

    def items(self):
        return ['index']
    
    def lastmod(self, obj):
        return obj.updated_at

    def location(self, item):
        return reverse(item)
