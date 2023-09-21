from django.contrib import admin
from adminsortable2.admin import SortableAdminBase
from images.admin import ImageInline
from railings.models import Railing
from common.admin import PageDescriptionAdmin, SimplePageAdmin


class RailingAdmin(SortableAdminBase, SimplePageAdmin, PageDescriptionAdmin):
    list_display = ('name',)
    inlines = [ImageInline,]

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Ограждения в стиле «Модерн»', {
                'fields': ('portfolio_title_m', 'portfolio_text_m',)
            }),
            ('Ограждения в стиле «Классика»', {
                'fields': ('portfolio_title_c', 'portfolio_text_c',)
            }),
            ('Ограждения в стиле «Ар-деко»', {
                'fields': ('portfolio_title_a', 'portfolio_text_a',)
            }),
            ('Ограждения в современном стиле', {
                'fields': ('portfolio_title_s', 'portfolio_text_s',)
            }),
        )
admin.site.register(Railing, RailingAdmin)
