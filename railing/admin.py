from django.contrib import admin
from common.admin import PageAdmin
from images.admin import ImageInline
from railing.models import Railing


class RailingAdmin(PageAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'menu_name', 'menu_order',)

admin.site.register(Railing, RailingAdmin)
