from django.db import models
from common.models import PageDescription, PageMenu, SimplePage
from django.contrib.contenttypes import fields
from images.models import Image


class Railing(SimplePage, PageDescription, PageMenu):
    portfolio_title_m = models.CharField('заголовок', blank=True, max_length=200)
    portfolio_text_m = models.TextField('текст', blank=True)
    @property
    def portfolio_images_m(self):
        return self.portfolio_images.filter(purpose='M')

    portfolio_title_c = models.CharField('заголовок', blank=True, max_length=200)
    portfolio_text_c = models.TextField('текст', blank=True)
    @property
    def portfolio_images_c(self):
        return self.portfolio_images.filter(purpose='C')

    portfolio_title_a = models.CharField('заголовок', blank=True, max_length=200)
    portfolio_text_a = models.TextField('текст', blank=True)
    @property
    def portfolio_images_a(self):
        return self.portfolio_images.filter(purpose='A')

    portfolio_title_s = models.CharField('заголовок', blank=True, max_length=200)
    portfolio_text_s = models.TextField('текст', blank=True)
    @property
    def portfolio_images_s(self):
        return self.portfolio_images.filter(purpose='S')

    portfolio_images = fields.GenericRelation(Image)

    class Meta:
        ordering = ('menu_order', )
        verbose_name = 'ограждение'
        verbose_name_plural = 'ограждения'