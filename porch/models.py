from django.db import models
from blocks.models import BlockSVG
from common.models import PageDescription, PageHWAW, PageMenu, PagePortfolio, SimplePage


class Porch(SimplePage, PageDescription, PageMenu, PagePortfolio, PageHWAW):
    class Meta:
        ordering = ('menu_order', )
        verbose_name = 'крыльцо'
        verbose_name_plural = 'крыльцо'
