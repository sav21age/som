from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from terraces.models import Terrace


class TerraceSitemap(Sitemap):
    priority = 1

    def items(self):
        return Terrace.objects.order_by('id')
    
    def lastmod(self, obj):
        return obj.updated_at

    # def location(self, item):
        # return reverse(item)

    # def location(self, item):
    #     return reverse('terrace')
