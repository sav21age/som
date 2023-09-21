from django.http import Http404
from django.shortcuts import render
from django.db.models import Prefetch
from django.core.exceptions import ObjectDoesNotExist
from staircases.models import Staircase
from images.models import Image
from videos.models import Video
from blocks.models import BlockImage, BlockPrice, BlockSVG


def staircase(request, slug):
    try:
        obj = Staircase.is_visible_objects.filter(slug=slug) \
            .select_related('typical_project') \
            .prefetch_related('hwaw') \
            .prefetch_related(Prefetch('block_svg', queryset=BlockSVG.is_visible_objects.all())) \
            .prefetch_related(Prefetch('block_price', queryset=BlockPrice.is_visible_objects.all())) \
            .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
            .prefetch_related(Prefetch('portfolio_videos', queryset=Video.is_visible_objects.all())) \
            .prefetch_related(Prefetch('block_railings', queryset=BlockImage.is_visible_objects.all())) \
            .get()
    except ObjectDoesNotExist as e:
        raise Http404 from e

    response = render(
        request,
        'staircases/index.html',
        {'object': obj, }
    )
    return response
