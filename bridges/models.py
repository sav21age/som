from django.db import models
from django.contrib.contenttypes import fields
from blocks.models import BlockSVG
from common.models import Page
from images.models import Image
from solo.models import SingletonModel


class Bridge(Page, SingletonModel):
    portfolio_images = fields.GenericRelation(Image)

    hwaw = models.ManyToManyField(
        BlockSVG, verbose_name='"Как мы работаем?"', related_name='+', 
        blank=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'мостик'
        verbose_name_plural = 'мостики'
