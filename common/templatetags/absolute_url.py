from django import template

register = template.Library()

@register.filter
def absolute_url(obj):
    print(obj._meta.app_label)
    return obj.get_absolute_url()
