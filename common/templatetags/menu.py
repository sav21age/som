from django import template
from menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def menu(context):
    qs = Menu.get_annotated_list()
    return {
        'menu': qs, 
        'cache_timeout': context['cache_timeout'], 
    }
