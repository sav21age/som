from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from easy_thumbnails.files import get_thumbnailer


class SVGAdminWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, 'url', None):
            result = '-'
            try:
                result = '<img src="{url}" width="{width}" height="{height}" style="background-color: rgb(121,174,200);">'.format(
                    url=value.url, width=64, height=64)
                output.append(result)
            except Exception as e:
                pass
        output.append(super(SVGAdminWidget, self).render(name, value, attrs))
        return mark_safe(''.join(output))
    

class IMGAdminWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        result = '-'
        try:
            thumbnailer = get_thumbnailer(value)
            thumb = thumbnailer.get_thumbnail(
                {'crop': 'scale', 'size': (100, 100)}).url
            result = '<a href="{i}" target="_blank" rel="noopener noreferrer"><img src="{t}" title="{i}"></a>'.format(
                        i=value.url,
                        t=thumb
            )
            output.append(result)
        except:
            pass
        output.append(super(IMGAdminWidget, self).render(name, value, attrs))

        return mark_safe(''.join(output))
