from django.contrib.contenttypes.admin import GenericStackedInline
from images.forms import ImageAdminForm
from images.models import Image
from django.forms import TextInput, Textarea
from django.db import models

formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'style': 'width: 70%; font-size: 115%;'})},
    models.TextField: {'widget': Textarea(attrs={'rows': 30, 'style': 'width: 70%; font-size: 115%;'})},
}

class ImageInline(GenericStackedInline):
    model = Image
    form = ImageAdminForm
    extra = 0
    show_change_link = True
    formfield_overrides = formfield_overrides
    verbose_name = "Наши работы - фотография"
    verbose_name_plural = "Наши работы - фотографии"
    