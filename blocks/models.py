import os
import random
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.images import get_image_path
from common.managers import IsVisibleManager
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Block(models.Model):
    is_visible = models.BooleanField('показывать', default=1, db_index=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

# --


class BlockText(Block):
    description = models.TextField('описание',)

    class Meta:
        verbose_name = 'текстовый блок'
        verbose_name_plural = 'текстовые блоки'

# --

class BlockPrice(Block):
    title = models.CharField('заголовок', max_length=200, unique=True)
    img_path = models.FileField(
        'путь к картинке', blank=True, null=True, upload_to=get_image_path,)

    price = models.PositiveIntegerField('цена, руб.',)

    class Meta:
        verbose_name = 'Блок с ценой'
        verbose_name_plural = 'Блоки с ценами'

# --


def validate_svg_path(value):
    ext_allowed = ['.svg',]
    f = os.path.splitext(value.name)
    if not f[1].lower() in ext_allowed:
        raise ValidationError('Неподдерживаемый тип файла.')


def get_svg_path(instance, filename):
    f = os.path.splitext(filename)
    return "blocks/svg/%s-%s.svg" % (f[0], random.randint(10000, 99999))


class BlockSVG(Block):
    block_name = models.CharField('название блока', max_length=80, blank=True)
    title = models.CharField('заголовок', max_length=200)
    description = models.TextField('описание',)
    order_number = models.PositiveSmallIntegerField(
        'порядковый номер', default=0,)
    svg_path = models.FileField('путь к svg файлу', upload_to=get_svg_path,
                                default='empty.svg', validators=[validate_svg_path],)

    def __str__(self):
        return '{0} - {1}'.format(self.block_name, self.title)

    class Meta:
        unique_together = ('block_name', 'title',)
        ordering = ['order_number']
        verbose_name = 'блок с векторной графикой'
        verbose_name_plural = 'блоки с векторной графикой'
