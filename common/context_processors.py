from django.conf import settings
from callback.forms import CallbackForm
from porch.models import Porch
from staircases.models import Staircase
from railings.models import Railing


menu = {
    'staircases': Staircase.is_visible_objects.only(
        'menu_name', 'slug').order_by('menu_order'),
    'railings': Railing.is_visible_objects.only(
        'menu_name', 'slug').order_by('menu_order'),
    'porch': Porch.is_visible_objects.only(
        'menu_name', 'slug').order_by('menu_order'),
}

def main(request):
    context = {
      'debug': settings.DEBUG,
      'cache_timeout': settings.CACHE_TIMEOUT,
      'rel_canonical': request.build_absolute_uri(),
      'menu': menu,
      'callback_form': CallbackForm(),
      'recaptcha_key': settings.RECAPTCHA_PUBLIC_KEY,
      'host': '{0}://{1}'.format(request.is_secure() and 'https' or 'http', request.get_host()),
    }
    return context
