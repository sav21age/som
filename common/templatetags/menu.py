from django import template
from menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def menu():
    qs = Menu.get_annotated_list()
    return {'menu': qs,}
