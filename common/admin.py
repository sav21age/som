from django.contrib import admin
from common.forms import SimplePageAdminForm
from images.admin import ImageInline
from videos.admin import VideoInline
from common.helpers import formfield_overrides

class SimplePageAdmin(admin.ModelAdmin):
    save_on_top = True
    form = SimplePageAdminForm
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


class PagePriceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, VideoInline,]
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Блок с ценами', {
                'fields': ('block_price_title', 'block_price',)
            }),
        )

class PageSVGAdmin(admin.ModelAdmin):
    inlines = [ImageInline, VideoInline,]
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Блок с векторной графикой', {
                'fields': ('block_svg_title', 'block_svg', )
            }),
        )


class PageRailingsAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Типовые варианты ограждений', {
                # 'fields': ('block_railings_title', 'block_railings',)
                'fields': ('block_railings',)
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

class PageCalculatorAdmin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Калькулятор', {
                'fields': ('is_calculator',)
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