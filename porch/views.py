from django.http import Http404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
from blocks.models import BlockImage
from porch.models import Porch
from images.models import Image
from videos.models import Video


def porch(request, slug):
    try:
        obj = Porch.is_visible_objects.filter(slug=slug) \
            .select_related('typical_project') \
            .prefetch_related('hwaw') \
            .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
            .prefetch_related(Prefetch('portfolio_videos', queryset=Video.is_visible_objects.all())) \
            .prefetch_related(Prefetch('block_railings', queryset=BlockImage.is_visible_objects.all())) \
            .get()
    except ObjectDoesNotExist as e:
        raise Http404 from e

    response = render(
        request,
        'porch/index.html',
        {'object': obj, }
    )
    return response
