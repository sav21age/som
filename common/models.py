import re
from django.db import models
from blocks.models import BlockImage, BlockPrice, BlockSVG
from common.managers import IsVisibleManager
from django.contrib.contenttypes import fields
from images.models import Image
from videos.models import Video
from common.helpers import quote, quote_office


class SimplePage(models.Model):
    head_title = models.CharField('title', max_length=80)
    meta_description = models.CharField('meta description', max_length=160)

    name = models.CharField('h1-название', max_length=80)
    slug = models.SlugField('url-адрес страницы', max_length=80, blank=False, unique=True)

    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('дата обновления', auto_now=True)
    is_visible = models.BooleanField('показывать', default=1, db_index=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return self.name
    
    def clean(self):
        self.head_title = re.sub(quote, r"«\1»", self.head_title)
        self.head_title = re.sub(quote_office, r"«\1»", self.head_title)
        self.meta_description = re.sub(quote, r"«\1»", self.meta_description)
        self.meta_description = re.sub(quote_office, r"«\1»", self.meta_description)

        self.name = re.sub(quote, r"«\1»", self.name)
        self.name = re.sub(quote_office, r"«\1»", self.name)

        # self.head_title = self.head_title.replace('"', "'")
        # self.meta_description = self.meta_description.replace('"', "'")
        super().clean()

    class Meta:
        abstract = True


class PageDescription(models.Model):
    description_title = models.CharField('заголовок', blank=True, max_length=200)
    description_text = models.TextField('текст', blank=True)

    def clean(self):
        if self.description_text:
            self.description_text = re.sub(quote_office, r"«\1»", self.description_text)
        super().clean()

    class Meta:
        abstract = True


class PageMenu(models.Model):
    menu_name = models.CharField('название для меню', max_length=80)
    menu_order = models.PositiveSmallIntegerField('порядковый номер в меню', default=0,)

    class Meta:
        abstract = True


class PagePortfolio(models.Model):
    portfolio_title = models.CharField('Заголовок', blank=True, max_length=200)
    portfolio_images = fields.GenericRelation(Image)
    portfolio_videos = fields.GenericRelation(Video)

    class Meta:
        abstract = True


class PagePrice(models.Model):
    block_price_title = models.CharField('Заголовок', blank=True, max_length=200)
    block_price = models.ManyToManyField(
        BlockPrice, verbose_name='объекты', related_name='+',
        blank=True, db_index=True)

    class Meta:
        abstract = True


class PageSVG(models.Model):
    block_svg_title = models.CharField(
        'заголовок', max_length=200, blank=True)
    block_svg = models.ManyToManyField(
        BlockSVG, verbose_name='объекты', related_name='block_svg',
        blank=True, db_index=True)

    class Meta:
        abstract = True


class PageRailings(models.Model):
    # block_railings_title = models.CharField('Заголовок', max_length=200, blank=True)
    block_railings = models.ManyToManyField(
        BlockImage, verbose_name='объекты', related_name='+',
        blank=True, db_index=True)

    class Meta:
        abstract = True


class PageHWAW(models.Model):
    hwaw = models.ManyToManyField(
        BlockSVG, verbose_name='объекты', related_name='+', 
        blank=True, db_index=True)

    class Meta:
        abstract = True


class PageCalculator(models.Model):
    is_calculator = models.BooleanField('показывать', default=1)

    class Meta:
        abstract = True


class TypicalProject(models.Model):
    name = models.CharField('название', max_length=250)

    def __str__(self):
        return self.name
    
    def clean(self):
        self.name = re.sub(quote, r"«\1»", self.name)
        self.name = re.sub(quote_office, r"«\1»", self.name)

        super().clean()

    class Meta:
        abstract = True
        verbose_name = 'типовой проект'
        verbose_name_plural = 'типовой проект'

    