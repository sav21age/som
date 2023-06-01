from django.http import Http404
from django.shortcuts import render
from staircases.models import Staircase


def staircase(request, slug):
    try:
        object = Staircase.is_visible_objects.filter(slug=slug) \
            .prefetch_related('hwaw') \
            .prefetch_related('prices') \
            .prefetch_related('block_svg') \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .get()
    except Staircase.DoesNotExist:
        raise Http404

    response = render(
        request,
        'staircases/index.html',
        {'object': object,}
    )
    return response
