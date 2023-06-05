from django.contrib import admin
from common.admin import SingletonPageAdmin
from index.models import IndexPage
from images.admin import ImageInline


class IndexPageAdmin(SingletonPageAdmin):
    inlines = [ImageInline, ]
    filter_horizontal = ('hwaw', 'prices', 'block_svg',)
    prepopulated_fields = {'slug': ('name', ),}

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        lst = []
        for t in fieldsets:
            if t[0] != 'Меню':
                lst.append(t)
        return tuple(lst) + (
            ('Блок с векторной графикой', {
                'fields': ('block_svg_title', 'block_svg', )
            }),
            ('Блок с ценами', {
                'fields': ('prices',)
            }),
            ('О компании', {
                'fields': ('about_title', 'about_text',)
            }),
            ('Как мы работаем?', {
                'fields': ('hwaw',)
            }),
            ('Наши работы', {
                'fields': ('portfolio_title',)
            }),
        )


admin.site.register(IndexPage, IndexPageAdmin)
