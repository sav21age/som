from django.db import models
from django.contrib.contenttypes import fields
from blocks.models import BlockPrice, BlockSVG
from common.models import Page
from images.models import Image
from videos.models import Video


class Staircase(Page):
    menu_name = models.CharField('название для меню', max_length=80, blank=True)
    menu_order = models.PositiveSmallIntegerField('порядковый номер в меню', default=0,)

    block_svg_title = models.CharField(
        'Заголовок', max_length=200, blank=True)
    block_svg = models.ManyToManyField(
        BlockSVG, verbose_name='"Контент"', related_name='block_svg',
        blank=True, db_index=True)

    prices = models.ManyToManyField(
        BlockPrice, verbose_name='"Цены"', related_name='+',
        blank=True, db_index=True)

    portfolio_images = fields.GenericRelation(Image)
    portfolio_videos = fields.GenericRelation(Video)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('menu_order', )
        verbose_name = 'лестницу'
        verbose_name_plural = 'лестницы'
