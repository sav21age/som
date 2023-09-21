from django.contrib.sitemaps import Sitemap
from railings.models import Railing


class RailingSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Railing.is_visible_objects.order_by('id').all()

    def lastmod(self, obj):
        return obj.updated_at

    # def location(self, obj):
    #     return reverse('railings:detail', kwargs={'slug': obj.slug})
