from django.contrib import admin
from solo.admin import SingletonModelAdmin
from calculator.models import Coeff, CoeffStaircaseType, RailingType, Service, StepsMaterialType
from common.helpers import formfield_overrides


class CoeffAdmin(SingletonModelAdmin):
    formfield_overrides = formfield_overrides


class CoeffStaircaseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_filter = ('is_visible',)
    formfield_overrides = formfield_overrides


class StepsMaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_filter = ('is_visible',)
    formfield_overrides = formfield_overrides


class RailingTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_filter = ('is_visible',)
    formfield_overrides = formfield_overrides

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_filter = ('is_visible',)
    formfield_overrides = formfield_overrides


admin.site.register(Coeff, CoeffAdmin)
admin.site.register(CoeffStaircaseType, CoeffStaircaseTypeAdmin)
admin.site.register(StepsMaterialType, StepsMaterialTypeAdmin)
admin.site.register(RailingType, RailingTypeAdmin)
admin.site.register(Service, ServiceAdmin)
