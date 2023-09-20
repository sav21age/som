from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from menu.models import Menu


class MenuAdmin(TreeAdmin):
    form = movenodeform_factory(Menu)

admin.site.register(Menu, MenuAdmin)