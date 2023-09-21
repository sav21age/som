from django import template
from calculator.forms import CalculatorForm

register = template.Library()


@register.inclusion_tag('calculator/calculator.html')
def calculator():
    form = CalculatorForm()
    return {'form': form,}
