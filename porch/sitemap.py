from django.contrib.sitemaps import Sitemap
from porch.models import Porch


class PorchSitemap(Sitemap):
    priority = 1

    def items(self):
        return Porch.is_visible_objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    # def location(self, obj):
    #     return reverse('porch:detail', kwargs={'slug': obj.slug})
