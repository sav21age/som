import re
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from common.managers import IsVisibleManager
from common.helpers import quote, quote_office


class Video(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    url = models.CharField('ссылка', max_length=255)
    title = models.CharField('аттрибут title', max_length=255, blank=True)
    order_number = models.PositiveSmallIntegerField('порядковый номер', default=0)
    is_visible = models.BooleanField('показывать', default=1, db_index=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return self.url

    def clean(self):
        if self.title: 
            self.title = re.sub(quote, r"«\1»", self.title)
            self.title = re.sub(quote_office, r"«\1»", self.title)
        
        # https://www.youtube.com/watch?v=iSDiBWMJb_I to https://www.youtube.com/embed/iSDiBWMJb_I
        self.url = self.url.replace('watch?v=', 'embed/')
        
        super().clean()

    class Meta:
        ordering = ('order_number',)
        verbose_name = 'видео'
        verbose_name_plural = 'видео'