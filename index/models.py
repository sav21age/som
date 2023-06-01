from django.db import models
from django.contrib.contenttypes import fields
from blocks.models import BlockPrice, BlockSVG
from common.models import Page
from images.models import Image
from solo.models import SingletonModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache.utils import make_template_fragment_key
from django.core.cache import caches, cache
from django.db.models.signals import post_save
from martor.models import MartorField


class IndexPage(Page, SingletonModel):
    block_svg_title = models.CharField(
        'Заголовок', max_length=200, blank=True)

    block_svg = models.ManyToManyField(
        BlockSVG, verbose_name='Контент', related_name='+',
        blank=True, db_index=True)

    hwaw = models.ManyToManyField(
        BlockSVG, verbose_name='"Как мы работаем?"', related_name='hwaw', 
        blank=True, db_index=True)

    prices = models.ManyToManyField(
        BlockPrice, verbose_name='"Цены"', related_name='prices',
        blank=True, db_index=True)

    # about_company = models.ForeignKey(
    #     BlockText, blank=True, null=True, on_delete=models.SET_NULL,
    #     verbose_name='о компании')
    
    about_title = models.CharField('Заголовок', blank=True, max_length=200)
    about_text = models.TextField('Текст', blank=True)
    # about_text = MartorField()

    portfolio_images = fields.GenericRelation(Image)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'главную страницу'
        verbose_name_plural = 'главные страницы'


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
