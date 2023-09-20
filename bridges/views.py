from django.http import Http404
from django.shortcuts import render
from django.db.models import Prefetch
from django.core.exceptions import ObjectDoesNotExist
from bridges.models import Bridge
from images.models import Image
from videos.models import Video


def bridges(request):
    try:
        obj = Bridge.objects \
        .prefetch_related('hwaw') \
        .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
        .prefetch_related(Prefetch('portfolio_videos', queryset=Video.is_visible_objects.all())) \
        .get()
    except ObjectDoesNotExist as e:
        raise Http404 from e

    response = render(
        request,
        'bridges/index.html',
        {'object': obj, }
    )
    return response
