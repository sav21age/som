from django import forms
from videos.models import Video
from videos.widgets import VideoAdminWidget


class VideoAdminForm(forms.ModelForm):
    class Meta:
        model = Video
        widgets = {
            'url': VideoAdminWidget(),
        }
        exclude = []