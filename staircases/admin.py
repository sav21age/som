from django.contrib import admin
from common.admin import PageCalculatorAdmin, PageHWAWAdmin, PageMenuAdmin, PageDescriptionAdmin, PagePortfolioAdmin, SimplePageAdmin
from staircases.models import Staircase


class StaircaseAdmin(SimplePageAdmin, PageCalculatorAdmin, PageHWAWAdmin, PagePortfolioAdmin, PageDescriptionAdmin, PageMenuAdmin):
    list_display = ('name', 'menu_name', 'menu_order',)
    filter_horizontal = ('hwaw', 'block_price', 'block_svg', )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('Блок с векторной графикой', {
                'fields': ('block_svg_title', 'block_svg', )
            }),
            ('Блок с ценами', {
                'fields': ('block_price',)
            }),
        )

admin.site.register(Staircase, StaircaseAdmin)
