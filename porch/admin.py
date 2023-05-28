from django.contrib import admin
from common.admin import PageAdmin
from images.admin import ImageInline
from porch.models import Porch


class PorchAdmin(PageAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'menu_name', 'menu_order',)

admin.site.register(Porch, PorchAdmin)
