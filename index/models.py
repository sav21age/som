from django.db import models
from django.urls import reverse
from blocks.models import BlockSVG
from solo.models import SingletonModel
from common.models import PageCalculator, PageDescription, PageHWAW, PagePortfolio, PagePrice, SimplePage


class Index(SimplePage, PageCalculator, PagePrice, PageDescription, PagePortfolio, PageHWAW, SingletonModel):
    block_svg_title = models.CharField(
        'заголовок', max_length=200, blank=True)
    block_svg = models.ManyToManyField(
        BlockSVG, verbose_name='объекты', related_name='+',
        blank=True, db_index=True)

    # block_price = models.ManyToManyField(
    #     BlockPrice, verbose_name='объекты', related_name='+',
    #     blank=True, db_index=True)

    about_title = models.CharField('заголовок', blank=True, max_length=200)
    about_text = models.TextField('текст', blank=True)

    class Meta:
        verbose_name = 'главная страница'
        verbose_name_plural = 'главные страницы'

    def get_absolute_url(self):
        return reverse('index')



# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.cache.utils import make_template_fragment_key
# from django.core.cache import caches, cache
# from django.db.models.signals import post_save

# @receiver(post_save, sender=IndexPage)
# def cache_invalidate(instance, **kwargs):
#     """ Rule of naming cache template fragment: time, model_name + fragment name, object_id, language_code """
#     if kwargs.get('raw'):  # add for test, pass fixtures
#         return

#     # print(instance._meta.app_label)
#     # key = make_template_fragment_key(
#     #     'images', [instance._meta.app_label, instance.id])
#     # caches['images'].delete(key)
#     # cache.delete()
#     # cache.clear()
#     caches['images'].clear()
