from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from index.models import Index


class IndexSitemap(Sitemap):
    priority = 1

    def items(self):
        # return ['index']
        return Index.objects.order_by('id')
    
    def lastmod(self, obj):
        return obj.updated_at

    # def location(self, item):
        # return reverse(item)

    def location(self, obj):
        return reverse('index')
