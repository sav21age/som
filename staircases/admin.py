from django.contrib import admin
from adminsortable2.admin import SortableAdminBase
from common.helpers import formfield_overrides
from common.admin import (
    PageCalculatorAdmin, PageHWAWAdmin, PageDescriptionAdmin, 
    PagePortfolioAdmin, PagePriceAdmin, PageRailingsAdmin, PageSVGAdmin,
    SimplePageAdmin
)
from staircases.models import Staircase, StaircaseTypicalProject


class StaircaseAdmin(
    SortableAdminBase, PagePortfolioAdmin, PagePriceAdmin, PageSVGAdmin,
    SimplePageAdmin, PageCalculatorAdmin, PageHWAWAdmin, PageRailingsAdmin,
    PageDescriptionAdmin):
    list_display = ('name',)
    filter_horizontal = ('hwaw', 'block_price', 'block_svg', 'block_railings', )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            # ('Блок с векторной графикой', {
            #     'fields': ('block_svg_title', 'block_svg', )
            # }),
            # ('Блок с ценами', {
            #     'fields': ('block_price',)
            # }),
            ('Типовой проект', {
                'fields': ('typical_project',)
            }),
        )

admin.site.register(Staircase, StaircaseAdmin)


class StaircaseTypicalProjectAdmin(admin.ModelAdmin):
    formfield_overrides = formfield_overrides

admin.site.register(StaircaseTypicalProject, StaircaseTypicalProjectAdmin)