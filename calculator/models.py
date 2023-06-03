from django.db import models
from solo.models import SingletonModel
from common.managers import IsVisibleManager

class Coeff(SingletonModel):
    h = models.PositiveSmallIntegerField('коэффициент высоты', default=0,)
    # delivery = models.PositiveIntegerField('доставка', default=0,)
    # installation = models.PositiveIntegerField('установка', default=0,)

    def __str__(self):
        return '{0}'.format(self.h)

    class Meta:
        verbose_name = 'коэффициент'
        verbose_name_plural = 'коэффициенты'

#--

class Type(models.Model):
    name = models.CharField('название', max_length=80)
    price = models.PositiveSmallIntegerField('цена', default=0,)
    order_number = models.PositiveSmallIntegerField('порядковый номер', default=0,)
    is_visible = models.BooleanField('показывать', default=1, db_index=True)

    objects = models.Manager()
    is_visible_objects = IsVisibleManager()

    def __str__(self):
        # return '{0} - {1}'.format(self.name, self.price)
        return '{0}'.format(self.name)

    class Meta:
        abstract = True


class CoeffStaircaseType(Type):
    class Meta:
        ordering = ['order_number']
        verbose_name = 'Коэффициент для типа лестницы'
        verbose_name_plural = 'Коэффициенты для типов лестницы'


class StepsMaterialType(Type):
    class Meta:
        ordering = ['order_number']
        verbose_name = 'тип материала ступеней'
        verbose_name_plural = 'тип материала ступеней'


class RailingType(Type):
    class Meta:
        ordering = ['order_number']
        verbose_name = 'тип ограждения'
        verbose_name_plural = 'тип ограждений'


class Service(Type):
    class Meta:
        ordering = ['order_number']
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

