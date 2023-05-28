from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from images.forms import ImageAdminForm
from images.models import Image


class ImageInline(GenericStackedInline):
    model = Image
    form = ImageAdminForm
    extra = 0
    show_change_link = True