from django.db import models
from blocks.models import BlockPrice, BlockSVG
from common.models import PageDescription, PageHWAW, PageMenu, PagePortfolio, SimplePage


class Staircase(SimplePage, PageDescription, PageMenu, PagePortfolio, PageHWAW):
    block_svg_title = models.CharField(
        'Заголовок', max_length=200, blank=True)
    block_svg = models.ManyToManyField(
        BlockSVG, verbose_name='"Контент"', related_name='block_svg',
        blank=True, db_index=True)

    block_price = models.ManyToManyField(
        BlockPrice, verbose_name='"Цены"', related_name='+',
        blank=True, db_index=True)

    class Meta:
        ordering = ('menu_order', )
        verbose_name = 'лестницу'
        verbose_name_plural = 'лестницы'
