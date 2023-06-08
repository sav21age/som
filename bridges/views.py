from django.http import Http404
from django.shortcuts import render
from bridges.models import Bridge
from django.db.models import Prefetch
from images.models import Image
from videos.models import Video


def bridges(request):
    try:
        object = Bridge.objects \
        .prefetch_related('hwaw') \
        .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
        .prefetch_related(Prefetch('portfolio_videos', queryset=Video.is_visible_objects.all())) \
        .get()
    except Bridge.DoesNotExist:
        raise Http404

    response = render(
        request,
        'bridges/index.html',
        {'object': object, }
    )
    return response
