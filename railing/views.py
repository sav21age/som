from django.http import Http404
from django.shortcuts import render
from railing.models import Railing


def railing(request, slug):
    try:
        object = Railing.is_visible_objects.filter(slug=slug) \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .get()
    except Railing.DoesNotExist:
        raise Http404

    response = render(
        request,
        'railing/index.html',
        {'object': object, }
    )
    return response
