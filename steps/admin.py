from django.contrib import admin
from common.admin import PageMenuAdmin, PageDescriptionAdmin, PagePortfolioAdmin, SimplePageAdmin
from steps.models import Steps


class StepsAdmin(SimplePageAdmin, PagePortfolioAdmin, PageDescriptionAdmin, PageMenuAdmin):
    list_display = ('name', 'menu_name', 'menu_order',)

admin.site.register(Steps, StepsAdmin)
