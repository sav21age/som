from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin
from images.admin import ImageInline
from videos.admin import VideoInline


formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'style': 'width: 70%; font-size: 115%;'})},
    models.TextField: {'widget': Textarea(attrs={'rows': 30, 'style': 'width: 70%; font-size: 115%;'})},
}

class SimplePageAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('name', )}
    formfield_overrides = formfield_overrides
    fieldsets = (
        ('', {
            'fields': ('is_visible',)
        }),
        ('Заголовок и мета теги страницы', {
            'fields': ('head_title', 'meta_description',)
        }),
        ('Имя и url-адрес страницы', {
            'fields': ('name', 'slug',)
        }),
    )


class PageMenuAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Меню', {
                'fields': ('menu_name', 'menu_order',)
            }),
        )


class PageDescriptionAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Описание', {
                'fields': ('description_title', 'description_text',)
            }),
        )


class PagePortfolioAdmin(admin.ModelAdmin):
    inlines = [ImageInline, VideoInline,]
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Наши работы', {
                'fields': ('portfolio_title',)
            }),
        )


class PageHWAWAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Как мы работаем?', {
                'fields': ('hwaw',)
            }),
        )


# fieldsets = (
#     ('Заголовок и мета теги страницы', {
#         'fields': ('head_title', 'meta_description', 'meta_keywords',)
#     }),
#     ('Имя и url-адрес страницы', {
#         'fields': ('name', 'slug',)
#     }),
#     ('Меню', {
#         'fields': ('menu_name', 'menu_order',)
#     }),
#     ('Описание', {
#         'fields': ('description_title', 'description_text',)
#     }),
# )


# class SingletonPageAdmin(SingletonModelAdmin):
#     save_on_top = True
#     prepopulated_fields = {'slug': ('name', )}
#     fieldsets = fieldsets
#     formfield_overrides = formfield_overrides


# class PageAdmin(admin.ModelAdmin):
#     save_on_top = True
#     prepopulated_fields = {'slug': ('name', )}
#     fieldsets = fieldsets
#     formfield_overrides = formfield_overrides