from django.contrib import admin
from solo.admin import SingletonModelAdmin
from common.admin import PageDescriptionAdmin, PageHWAWAdmin, PagePortfolioAdmin, SimplePageAdmin
from terraces.models import Terrace


class TerraceAdmin(SimplePageAdmin, PageHWAWAdmin, PagePortfolioAdmin, PageDescriptionAdmin, SingletonModelAdmin):
    filter_horizontal = ('hwaw',)

admin.site.register(Terrace, TerraceAdmin)
