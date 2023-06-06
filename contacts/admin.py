from django.contrib import admin
from contacts.models import ContactPage
from common.admin import SimplePageAdmin
from solo.admin import SingletonModelAdmin


class ContactPageAdmin(SimplePageAdmin, SingletonModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Контактная информация', {
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

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['address_showroom_map'].widget.attrs['rows'] = 7
        form.base_fields['address_production_map'].widget.attrs['rows'] = 7
        return form

admin.site.register(ContactPage, ContactPageAdmin)
