from django.http import Http404
from django.shortcuts import render
from steps.models import Steps


def steps(request, slug):
    try:
        object = Steps.is_visible_objects.filter(slug=slug) \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .get()
    except Steps.DoesNotExist:
        raise Http404

    response = render(
        request,
        'steps/index.html',
        {'object': object, }
    )
    return response
