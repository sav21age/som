from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from common.models import SimplePage
from solo.models import SingletonModel


class Contacts(SimplePage, SingletonModel):
    address_showroom = models.CharField(
        'адрес выставочного зала', max_length=200, null=True, blank=True)
    address_showroom_map = models.TextField(
        'карта проезда до выставочного зала', null=True, blank=True)
    
    address_production = models.CharField(
        'адрес производства', max_length=200, null=True, blank=True)
    address_production_map = models.TextField(
        'карта проезда к производству', null=True, blank=True)

    phone = models.CharField('телефон', max_length=20, null=True, blank=True)
    email = models.CharField('email', max_length=50, null=True, blank=True)

    work_schedule = models.CharField(
        'график работы', max_length=50, null=True, blank=True)

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'

    def get_absolute_url(self):
        return reverse('contacts')
