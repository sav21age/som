from solo.admin import SingletonModelAdmin
from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin
# from martor.widgets import AdminMartorWidget


formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'style': 'width: 70%; font-size: 115%;'})},
    models.TextField: {'widget': Textarea(attrs={'rows': 30, 'style': 'width: 70%; font-size: 115%;'})},
    # models.TextField: {'widget': AdminMartorWidget},
}

fieldsets = (
    ('Заголовок и мета теги страницы', {
        'fields': ('head_title', 'meta_description', 'meta_keywords',)
    }),
    ('Имя и url-адрес страницы', {
        'fields': ('name', 'slug',)
    }),
    ('Меню', {
        'fields': ('menu_name', 'menu_order',)
    }),
    ('Описание', {
        'fields': ('description_title', 'description_text',)
    }),
)


class SingletonPageAdmin(SingletonModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('name', )}
    fieldsets = fieldsets
    formfield_overrides = formfield_overrides


class PageAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('name', )}
    fieldsets = fieldsets
    formfield_overrides = formfield_overrides
