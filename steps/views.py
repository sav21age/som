from django.http import Http404
from django.shortcuts import render
from steps.models import Steps
from django.db.models import Prefetch
from images.models import Image
from videos.models import Video


def steps(request, slug):
    try:
        object = Steps.is_visible_objects.filter(slug=slug) \
            .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
            .prefetch_related(Prefetch('portfolio_videos', queryset=Video.is_visible_objects.all())) \
            .get()
    except Steps.DoesNotExist:
        raise Http404

    response = render(
        request,
        'steps/index.html',
        {'object': object, }
    )
    return response
