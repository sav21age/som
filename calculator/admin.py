from django.contrib import admin
from django.forms import NumberInput, TextInput
from solo.admin import SingletonModelAdmin
from calculator.models import Coeff, CoeffStaircaseType, RailingType, Service, StepsMaterialType
from django.db import models


formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'style': 'width: 70%; font-size: 115%;'})},
    models.IntegerField: {'widget': NumberInput(attrs={'style': 'width: 100px; font-size: 115%;'})},
}

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
