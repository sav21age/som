from django.http import Http404
from django.shortcuts import render
from porch.models import Porch
from django.db.models import Prefetch
from images.models import Image
from videos.models import Video


def porch(request, slug):
    try:
        object = Porch.objects.filter(slug=slug) \
            .prefetch_related('hwaw') \
            .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
            .prefetch_related(Prefetch('portfolio_videos', queryset=Video.is_visible_objects.all())) \
            .get()
    except Porch.DoesNotExist:
        raise Http404

    response = render(
        request,
        'porch/index.html',
        {'object': object, }
    )
    return response
