from django.conf import settings
from callback.forms import CallbackForm
from porch.models import Porch
from staircases.models import Staircase
from railing.models import Railing
from steps.models import Steps

menu = {
    'staircases': Staircase.objects.only(
        'menu_name', 'slug').order_by('menu_order'),
    'railing': Railing.objects.only(
        'menu_name', 'slug').order_by('menu_order'),
    'steps': Steps.objects.only(
        'menu_name', 'slug').order_by('menu_order'),
    'porch': Porch.objects.only(
        'menu_name', 'slug').order_by('menu_order'),
}

def main(request):
    context = {
      'debug': settings.DEBUG,
      'cache_timeout': settings.CACHE_TIMEOUT,
      'menu': menu,
      'callback_form': CallbackForm(),
      'recaptcha_key': settings.RECAPTCHA_PUBLIC_KEY,
      'host': '{0}://{1}'.format(request.is_secure() and 'https' or 'http', request.get_host()),
    }
    return context
