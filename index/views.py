from django.http import Http404
from django.shortcuts import render
from index.models import IndexPage
from calculator.forms import CalculatorForm


def index(request):
    try:
        object = IndexPage.objects \
            .prefetch_related('block_svg') \
            .prefetch_related('hwaw') \
            .prefetch_related('prices') \
            .prefetch_related('portfolio_images') \
            .prefetch_related('portfolio_videos') \
            .get()
    except IndexPage.DoesNotExist:
        raise Http404

    response = render(
        request,
        'index/index.html',
        {'object': object, 'form': CalculatorForm(),}
    )
    return response
