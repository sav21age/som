from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes import fields
from blocks.models import BlockText
from common.models import SimplePage
from images.models import Image
from solo.models import SingletonModel

# class Address(models.Model):
#     title = models.CharField(_("title"), max_length=30)
#     address = models.TextField(_("address"),)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = _('address')
#         verbose_name_plural = _('addresses')


# class Phone(models.Model):
#     title = models.CharField(_("title"), max_length=30)
#     number = models.TextField(_("number"),)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = _('phone')
#         verbose_name_plural = _('phones')


# class Email(models.Model):
#     title = models.CharField(_("title"), max_length=30)
#     email = models.TextField(_("email"),)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = _('email')
#         verbose_name_plural = _('emails')


class ContactPage(SimplePage, SingletonModel):
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

    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    # phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    # email = models.ForeignKey(Email, on_delete=models.CASCADE)

    work_schedule = models.CharField(
        'график работы', max_length=50, null=True, blank=True)


    images = fields.GenericRelation(Image, verbose_name="картинки")

    def __str__(self):
        return self.address_showroom

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'
