from django.contrib import admin
from common.admin import SingletonPageAdmin
from bridges.models import Bridge
from images.admin import ImageInline


class BridgeAdmin(SingletonPageAdmin):
    inlines = [ImageInline]
    prepopulated_fields = {'slug': ('name', )}
    filter_horizontal = ('hwaw',)

    fieldsets = (
        ('Заголовок и мета теги страницы', {
            'fields': ('head_title', 'meta_description', 'meta_keywords',)
        }),
        ('Имя и url-адрес страницы', {
            'fields': ('name', 'slug',)
        }),
        ('Описание', {
            'fields': ('description_title', 'description_text',)
        }),
        ('Как мы работаем?', {
            'fields': ('hwaw',)
        }),
        ('Наши работы', {
            'fields': ('portfolio_title',)
        }),
    )

admin.site.register(Bridge, BridgeAdmin)
