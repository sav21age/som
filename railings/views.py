from django.http import Http404
from django.shortcuts import render
from railings.models import Railing
from django.db.models import Prefetch
from images.models import Image
from videos.models import Video


def railings(request, slug):
    try:
        object = Railing.is_visible_objects.filter(slug=slug) \
            .prefetch_related(Prefetch('portfolio_images', queryset=Image.is_visible_objects.all())) \
            .get()
    except Railing.DoesNotExist:
        raise Http404

    response = render(
        request,
        'railings/index.html',
        {'object': object, }
    )
    return response
