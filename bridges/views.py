from django.http import Http404
from django.shortcuts import render
from bridges.models import Bridge


def bridges(request):
    try:
        object = Bridge.objects.prefetch_related('hwaw').get()
    except Bridge.DoesNotExist:
        raise Http404

    response = render(
        request,
        'bridges/index.html',
        {'object': object, }
    )
    return response
