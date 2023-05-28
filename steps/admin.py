from django.contrib import admin
from common.admin import PageAdmin
from images.admin import ImageInline
from steps.models import Steps


class StepsAdmin(PageAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'menu_name', 'menu_order',)

admin.site.register(Steps, StepsAdmin)
