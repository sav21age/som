from django.contrib import admin
from common.admin import SingletonPageAdmin
from bridges.models import Bridge
from images.admin import ImageInline


class BridgeAdmin(SingletonPageAdmin):
    inlines = [ImageInline]
    prepopulated_fields = {'slug': ('name', )}
    filter_horizontal = ('hwaw',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        lst = []
        for t in fieldsets:
            if t[0] != 'Меню':
                lst.append(t)
        return tuple(lst) + (
            ('Как мы работаем?', {
                'fields': ('hwaw',)
            }),
        )

admin.site.register(Bridge, BridgeAdmin)
