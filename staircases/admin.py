from django.contrib import admin
from common.admin import PageAdmin
from images.admin import ImageInline
from staircases.models import Staircase
from videos.admin import VideoInline


class StaircaseAdmin(PageAdmin):
    inlines = [ImageInline, VideoInline,]
    list_display = ('name', 'menu_name', 'menu_order',)
    filter_horizontal = ('hwaw', 'prices', 'block_svg', )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Блок с векторной графикой', {
                'fields': ('block_svg_title', 'block_svg', )
            }),
            ('Блок с ценами', {
                'fields': ('prices',)
            }),
            ('Как мы работаем?', {
                'fields': ('hwaw',)
            }),
        )

admin.site.register(Staircase, StaircaseAdmin)
