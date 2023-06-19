from django.contrib.contenttypes.admin import GenericStackedInline
from videos.forms import VideoAdminForm
from videos.models import Video
from common.helpers import formfield_overrides

class VideoInline(GenericStackedInline):
    model = Video
    form = VideoAdminForm
    extra = 0
    show_change_link = True
    formfield_overrides = formfield_overrides
    verbose_name = "Наши работы - видео"
    verbose_name_plural = "Наши работы - видео"
