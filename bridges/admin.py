from django.contrib import admin
from solo.admin import SingletonModelAdmin
from bridges.models import Bridge
from common.admin import (
    PageDescriptionAdmin, PageHWAWAdmin, PagePortfolioAdmin, SimplePageAdmin
)
from adminsortable2.admin import SortableAdminBase


class BridgeAdmin(SortableAdminBase, SimplePageAdmin, PageHWAWAdmin, PagePortfolioAdmin, PageDescriptionAdmin, SingletonModelAdmin):
    filter_horizontal = ('hwaw',)

admin.site.register(Bridge, BridgeAdmin)
