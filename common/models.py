from django.db import models
from common.managers import IsVisibleManager


class SimplePage(models.Model):
    head_title = models.CharField('title', max_length=80)
    meta_description = models.CharField('meta description', max_length=160)
    meta_keywords = models.CharField('meta keywords', max_length=160)

    name = models.CharField('название', max_length=80)
    slug = models.SlugField('url-адрес страницы', max_length=80, blank=False, unique=True)

    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('дата обновления', auto_now=True)
    is_visible = models.BooleanField('показывать', default=1, db_index=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    class Meta:
        abstract = True

  
class Page(SimplePage):
    description_title = models.CharField('Заголовок', blank=True, max_length=200)
    description_text = models.TextField('Текст', blank=True)

    class Meta:
        abstract = True
