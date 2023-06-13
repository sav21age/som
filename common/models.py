import re
from django.db import models
from blocks.models import BlockSVG
from common.managers import IsVisibleManager
from django.contrib.contenttypes import fields
from images.models import Image
from videos.models import Video

quote = re.compile(r'\"(.*?)\"')
quote_office = re.compile(r'\“(.*?)\”')


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
    description_title = models.CharField('Заголовок', blank=True, max_length=200)
    description_text = models.TextField('Текст', blank=True)

    def clean(self):
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
    # portfolio_title = models.CharField('Заголовок', blank=True, max_length=200)
    portfolio_images = fields.GenericRelation(Image)
    portfolio_videos = fields.GenericRelation(Video)

    class Meta:
        abstract = True


class PageHWAW(models.Model):
    hwaw = models.ManyToManyField(
        BlockSVG, verbose_name='"Как мы работаем?"', related_name='+', 
        blank=True, db_index=True)

    class Meta:
        abstract = True

class PageCalculator(models.Model):
    is_calculator = models.BooleanField('показывать', default=1)

    class Meta:
        abstract = True