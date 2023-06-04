from django.contrib import admin
from common.admin import PageAdmin
from images.admin import ImageInline
from steps.models import Steps


class StepsAdmin(PageAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'menu_name', 'menu_order',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        lst = []
        for t in fieldsets:
            if t[0] != 'Меню':
                lst.append(t)
        return tuple(lst) + (
            ('Наши работы', {
                'fields': ('portfolio_title',)
            }),
        )


admin.site.register(Steps, StepsAdmin)
