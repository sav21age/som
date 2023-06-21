from django.contrib import admin
from porch.models import Porch, PorchTypicalProject
from common.admin import PageHWAWAdmin, PageMenuAdmin, PageDescriptionAdmin, PagePortfolioAdmin, PageRailingsAdmin, SimplePageAdmin
from common.helpers import formfield_overrides


class PorchAdmin(SimplePageAdmin, PageHWAWAdmin, PageRailingsAdmin, PagePortfolioAdmin, PageDescriptionAdmin, PageMenuAdmin):
    list_display = ('name', 'menu_name', 'menu_order',)
    filter_horizontal = ('hwaw', 'block_railings', )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Типовой проект', {
                'fields': ('typical_project',)
            }),
        )

admin.site.register(Porch, PorchAdmin)


class PorchTypicalProjectAdmin(admin.ModelAdmin):
    formfield_overrides = formfield_overrides

admin.site.register(PorchTypicalProject, PorchTypicalProjectAdmin)