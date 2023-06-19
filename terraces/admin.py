from django.contrib import admin
from solo.admin import SingletonModelAdmin
from common.admin import PageDescriptionAdmin, PageHWAWAdmin, PagePortfolioAdmin, PageRailingsAdmin, SimplePageAdmin
from terraces.models import Terrace, TerraceTypicalProject
from common.helpers import formfield_overrides


class TerraceAdmin(SimplePageAdmin, PageHWAWAdmin, PageRailingsAdmin, PagePortfolioAdmin, PageDescriptionAdmin, SingletonModelAdmin):
    filter_horizontal = ('hwaw', 'block_railings', )

admin.site.register(Terrace, TerraceAdmin)


class TerraceTypicalProjectAdmin(SingletonModelAdmin):
    formfield_overrides = formfield_overrides

admin.site.register(TerraceTypicalProject, TerraceTypicalProjectAdmin)