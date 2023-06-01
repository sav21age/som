from django.contrib.admin.widgets import AdminURLFieldWidget
from django.utils.safestring import mark_safe


# Usage: AdminWidget()
class VideoAdminWidget(AdminURLFieldWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        result = ''
        if value:
            result = '<iframe src="{}" allowfullscreen></iframe>'.format(value)
        output.append(result)
        output.append(super(VideoAdminWidget, self).render(name, value, attrs))
        return mark_safe(''.join(output))