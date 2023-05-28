from django.db import models
from django.contrib.contenttypes import fields
from common.models import Page
from images.models import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.cache import cache


class Porch(Page):
    menu_name = models.CharField(
        'название для меню', max_length=80, blank=True)
    menu_order = models.PositiveSmallIntegerField(
        'порядковый номер в меню', default=0,)

    portfolio = fields.GenericRelation(Image)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('menu_order', )
        verbose_name = 'крыльцо'
        verbose_name_plural = 'крыльцо'
