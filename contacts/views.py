from django.http import Http404
from django.shortcuts import render
from contacts.models import ContactPage


def contacts(request):
    try:
        object = ContactPage.objects.get()
    except ContactPage.DoesNotExist:
        raise Http404

    response = render(
        request,
        'contacts/index.html',
        {'object': object, }
    )
    return response
