from django.contrib import admin
from solo.admin import SingletonModelAdmin
from bridges.models import Bridge
from common.admin import PageDescriptionAdmin, PageHWAWAdmin, PagePortfolioAdmin, SimplePageAdmin


class BridgeAdmin(SimplePageAdmin, PageHWAWAdmin, PagePortfolioAdmin, PageDescriptionAdmin, SingletonModelAdmin):
    filter_horizontal = ('hwaw',)

admin.site.register(Bridge, BridgeAdmin)
