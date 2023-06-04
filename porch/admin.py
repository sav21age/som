from django.contrib import admin
from common.admin import PageAdmin
from images.admin import ImageInline
from porch.models import Porch


class PorchAdmin(PageAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'menu_name', 'menu_order',)
    filter_horizontal = ('hwaw',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Как мы работаем?', {
                'fields': ('hwaw',)
            }),
            ('Наши работы', {
                'fields': ('portfolio_title',)
            }),
        )
    
admin.site.register(Porch, PorchAdmin)
