from django.http import Http404
from django.shortcuts import render
from django.db.models import Prefetch
from staircases.models import Staircase
from images.models import Image
from videos.models import Video
from blocks.models import BlockImage, BlockPrice, BlockSVG
from calculator.forms import CalculatorForm


def staircase(request, slug):
    try:
        object = Staircase.is_visible_objects.filter(slug=slug) \
            .prefetch_related('hwaw') \
            .prefetch_related(Prefetch('block_svg', queryset=BlockSVG.is_visible_objects.all())) \
            .prefetch_related(Prefetch('block_price', queryset=BlockPrice.is_visible_objects.all())) \
            .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
            .prefetch_related(Prefetch('portfolio_videos', queryset=Video.is_visible_objects.all())) \
            .prefetch_related(Prefetch('block_railings', queryset=BlockImage.is_visible_objects.all())) \
            .get()
    except Staircase.DoesNotExist:
        raise Http404

    response = render(
        request,
        'staircases/index.html',
        {'object': object, 'form': CalculatorForm(),}
    )
    return response
