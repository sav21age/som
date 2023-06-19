from django.contrib.contenttypes.admin import GenericStackedInline
from images.forms import ImageAdminForm
from images.models import Image
from common.helpers import formfield_overrides

class ImageInline(GenericStackedInline):
    model = Image
    form = ImageAdminForm
    extra = 0
    show_change_link = True
    formfield_overrides = formfield_overrides
    verbose_name = "Наши работы - фотография"
    verbose_name_plural = "Наши работы - фотографии"
    