import os
import re
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.helpers import get_image_path, get_svg_path
from common.managers import IsVisibleManager
from common.helpers import quote, quote_office

class Block(models.Model):
    title = models.CharField('заголовок', max_length=200)

    is_visible = models.BooleanField('показывать', default=1, db_index=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        return self.title
    
    def clean(self):
        self.title = re.sub(quote, r"«\1»", self.title)
        self.title = re.sub(quote_office, r"«\1»", self.title)
        super().clean()

    class Meta:
        abstract = True

# --


class BlockText(Block):
    description = models.TextField('описание',)

    class Meta:
        verbose_name = 'текстовый блок'
        verbose_name_plural = 'текстовые блоки'

# --

class BlockIMG(Block):
    img_path = models.FileField(
        'путь к картинке', blank=True, null=True, upload_to=get_image_path,)
    upload_to_dir = 'blocks'

    class Meta:
        abstract = True


class BlockImage(BlockIMG):
    block_name = models.CharField('название блока', max_length=80, blank=True)
    is_zoom = models.BooleanField('увеличивать', default=1, db_index=True)
    order_number = models.PositiveSmallIntegerField(
        'порядковый номер', default=0,)

    def __str__(self):
        return '{0} - {1}'.format(self.block_name, self.title)
    
    def clean(self):
        self.block_name = re.sub(quote, r"«\1»", self.block_name)
        self.block_name = re.sub(quote_office, r"«\1»", self.block_name)
        super().clean()

    class Meta:
        unique_together = ('block_name', 'title',)
        ordering = ['order_number']
        verbose_name = 'Блок с картинкой'
        verbose_name_plural = 'Блоки с картинками'


class BlockPrice(BlockIMG):
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


class BlockSVG(Block):
    block_name = models.CharField('название блока', max_length=80, blank=True)
    description = models.TextField('описание',)
    order_number = models.PositiveSmallIntegerField(
        'порядковый номер', default=0,)
    svg_path = models.FileField('путь к svg файлу', upload_to=get_svg_path,
                                default='empty.svg', validators=[validate_svg_path],)

    def __str__(self):
        return '{0} - {1}'.format(self.block_name, self.title)
    
    def clean(self):
        self.block_name = re.sub(quote, r"«\1»", self.block_name)
        self.block_name = re.sub(quote_office, r"«\1»", self.block_name)
        super().clean()

    class Meta:
        unique_together = ('block_name', 'title',)
        ordering = ['order_number']
        verbose_name = 'блок с векторной графикой'
        verbose_name_plural = 'блоки с векторной графикой'
