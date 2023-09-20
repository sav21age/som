from django.contrib import admin
from solo.admin import SingletonModelAdmin
from common.admin import PageDescriptionAdmin, PageHWAWAdmin, PagePortfolioAdmin, PageRailingsAdmin, SimplePageAdmin
from terraces.models import Terrace, TerraceTypicalProject
from common.helpers import formfield_overrides
from adminsortable2.admin import SortableAdminBase


class TerraceAdmin(SortableAdminBase, SimplePageAdmin, PageHWAWAdmin, PageRailingsAdmin, PagePortfolioAdmin, PageDescriptionAdmin, SingletonModelAdmin):
    filter_horizontal = ('hwaw', 'block_railings', )
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Типовой проект', {
                'fields': ('typical_project',)
            }),
        )

admin.site.register(Terrace, TerraceAdmin)


class TerraceTypicalProjectAdmin(admin.ModelAdmin):
    formfield_overrides = formfield_overrides

admin.site.register(TerraceTypicalProject, TerraceTypicalProjectAdmin)