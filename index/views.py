from django.http import Http404
from django.shortcuts import render
from index.models import Index
from calculator.forms import CalculatorForm


def index(request):
    try:
        object = Index.objects \
            .prefetch_related('block_svg') \
            .prefetch_related('hwaw') \
            .prefetch_related('prices') \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .get()
    except Index.DoesNotExist:
        raise Http404

    response = render(
        request,
        'index/index.html',
        {'object': object, 'form': CalculatorForm(),}
    )
    return response
