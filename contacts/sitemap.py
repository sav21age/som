from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class ContactsSitemap(Sitemap):

    def items(self):
        return ['contacts']
    
    def lastmod(self, obj):
        return obj.updated_at

    def location(self, item):
        return reverse(item)
