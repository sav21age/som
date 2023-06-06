from django.contrib import admin
from porch.models import Porch
from common.admin import PageHWAWAdmin, PageMenuAdmin, PageDescriptionAdmin, PagePortfolioAdmin, SimplePageAdmin


class PorchAdmin(SimplePageAdmin, PageHWAWAdmin, PagePortfolioAdmin, PageDescriptionAdmin, PageMenuAdmin):
    list_display = ('name', 'menu_name', 'menu_order',)
    filter_horizontal = ('hwaw',)

admin.site.register(Porch, PorchAdmin)
