from django.http import Http404
from django.shortcuts import render
from porch.models import Porch


def porch(request, slug):
    try:
        object = Porch.objects.filter(slug=slug) \
            .prefetch_related('hwaw') \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .get()
    except Porch.DoesNotExist:
        raise Http404

    response = render(
        request,
        'porch/index.html',
        {'object': object, }
    )
    return response
