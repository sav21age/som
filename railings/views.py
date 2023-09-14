from django.http import Http404
from django.shortcuts import render
from django.db.models import Prefetch
from django.core.exceptions import ObjectDoesNotExist
from railings.models import Railing
from images.models import Image


def railings(request, slug):
    try:
        obj = Railing.is_visible_objects.filter(slug=slug) \
            .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
            .get()
    except ObjectDoesNotExist as e:
        raise Http404 from e

    response = render(
        request,
        'railings/index.html',
        {'object': obj, }
    )
    return response
