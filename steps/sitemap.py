from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from steps.models import Steps


class StepsSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Steps.is_visible_objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('steps:detail', kwargs={'slug': obj.slug})
