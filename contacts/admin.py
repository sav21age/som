from django.contrib import admin
from contacts.models import ContactPage
from common.admin import SingletonPageAdmin


class ContactPageAdmin(SingletonPageAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        lst = []
        for t in fieldsets:
            if t[0] != 'Описание':
                lst.append(t)
        return tuple(lst) + (
            ('', {
                'fields': (
                    'phone',
                    'email',
                    'work_schedule',
                    'address_showroom',
                    'address_showroom_map',
                    'address_production',
                    'address_production_map',
                )
            }),
        )


admin.site.register(ContactPage, ContactPageAdmin)
