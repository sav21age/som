from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from contacts.models import ContactPage


class ContactsSitemap(Sitemap):
    priority = 0.5
    
    def items(self):
        # return ['contacts']
        return ContactPage.is_visible_objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at

    # def location(self, item):
        # return reverse(item)

    def location(self, obj):
        return reverse('contacts')
