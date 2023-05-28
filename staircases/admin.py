from django.contrib import admin
from common.admin import PageAdmin
from images.admin import ImageInline
from staircases.models import Staircase


class StaircaseAdmin(PageAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'menu_name', 'menu_order',)
    filter_horizontal = ('prices', 'block_svg', )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Блок с ценами', {
                'fields': ('prices',)
            }),
            ('Блок с векторной графикой', {
                'fields': ('block_svg_title', 'block_svg', )
            }),
        )

admin.site.register(Staircase, StaircaseAdmin)
