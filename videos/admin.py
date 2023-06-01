from django.contrib.contenttypes.admin import GenericStackedInline
from videos.forms import VideoAdminForm
from videos.models import Video

class VideoInline(GenericStackedInline):
    model = Video
    form = VideoAdminForm
    extra = 0
    show_change_link = True
