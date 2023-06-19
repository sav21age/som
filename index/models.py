from django.db import models
from blocks.models import BlockPrice, BlockSVG
from solo.models import SingletonModel
from common.models import PageCalculator, PageDescription, PageHWAW, PagePortfolio, SimplePage


class Index(SimplePage, PageCalculator, PageDescription, PagePortfolio, PageHWAW, SingletonModel):
    block_svg_title = models.CharField(
        'Заголовок', max_length=200, blank=True)
    block_svg = models.ManyToManyField(
        BlockSVG, verbose_name='Контент', related_name='+',
        blank=True, db_index=True)

    block_price = models.ManyToManyField(
        BlockPrice, verbose_name='"Цены"', related_name='+',
        blank=True, db_index=True)

    about_title = models.CharField('Заголовок', blank=True, max_length=200)
    about_text = models.TextField('Текст', blank=True)
    
    class Meta:
        verbose_name = 'главная страница'
        verbose_name_plural = 'главные страницы'


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
