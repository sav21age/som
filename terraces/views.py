from django.http import Http404
from django.shortcuts import render
from django.db.models import Prefetch
from images.models import Image
from terraces.models import Terrace
from videos.models import Video


def terraces(request):
    try:
        object = Terrace.objects \
        .prefetch_related('hwaw') \
        .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
        .prefetch_related(Prefetch('portfolio_videos', queryset=Video.is_visible_objects.all())) \
        .get()
    except Terrace.DoesNotExist:
        raise Http404

    response = render(
        request,
        'terraces/index.html',
        {'object': object, }
    )
    return response