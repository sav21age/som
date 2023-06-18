from django.contrib import admin
from railings.models import Railing
from common.admin import PageMenuAdmin, PageDescriptionAdmin, PagePortfolioAdmin, SimplePageAdmin

class RailingAdmin(SimplePageAdmin, PagePortfolioAdmin, PageDescriptionAdmin, PageMenuAdmin):
    list_display = ('name', 'menu_name', 'menu_order',)

admin.site.register(Railing, RailingAdmin)
