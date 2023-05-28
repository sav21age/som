from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from easy_thumbnails.fields import ThumbnailerImageField
from common.images import get_image_path
from common.managers import IsVisibleManager
from django.core.cache import cache


class Image(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    path = ThumbnailerImageField(
        'Путь к картинке',
        blank=True,
        max_length=200,
        upload_to=get_image_path,
        resize_source={'size': (800, 800), 'crop': 'scale'}
    )

    alt = models.CharField('аттрибут alt', max_length=200, null=True, blank=True, )
    title = models.CharField('аттрибут title', max_length=200, null=True, blank=True, )
    order_number = models.PositiveSmallIntegerField('порядковый номер', default=0)
    is_visible = models.BooleanField('показывать', default=1, db_index=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return self.path.path

    class Meta:
        ordering = ('order_number',)
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'


# @receiver(post_save, sender=Image)
# def save_as(instance, **kwargs):
#     """Delete empty images after _saveasnew in admin was called."""
#     if kwargs.get('raw'):  # add for test, pass fixtures
#         return
#     Image.objects.filter(path__exact='').delete()

@receiver(post_save, sender=Image)
def cache_invalidate(instance, **kwargs):
    if kwargs.get('raw'):  # add for test, pass fixtures
        return
    
    # cache.delete('images')
    # cache.delete_many(keys=cache.keys('images*'))
    cache.clear()
