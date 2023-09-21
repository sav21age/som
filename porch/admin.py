from django.contrib import admin
from adminsortable2.admin import SortableAdminBase
from porch.models import Porch, PorchTypicalProject
from common.admin import (
    PageHWAWAdmin, PageDescriptionAdmin, PagePortfolioAdmin,
    PageRailingsAdmin, SimplePageAdmin
)
from common.helpers import formfield_overrides


class PorchAdmin(
    SortableAdminBase, SimplePageAdmin, PageHWAWAdmin,
    PageRailingsAdmin, PagePortfolioAdmin, PageDescriptionAdmin):
    list_display = ('name',)
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
