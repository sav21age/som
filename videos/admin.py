from django.contrib.contenttypes.admin import GenericStackedInline
from videos.forms import VideoAdminForm
from videos.models import Video
from django.forms import TextInput, Textarea
from django.db import models


formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'style': 'width: 70%; font-size: 115%;'})},
    models.TextField: {'widget': Textarea(attrs={'rows': 30, 'style': 'width: 70%; font-size: 115%;'})},
}

class VideoInline(GenericStackedInline):
    model = Video
    form = VideoAdminForm
    extra = 0
    show_change_link = True
    formfield_overrides = formfield_overrides