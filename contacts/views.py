from django.http import Http404
from django.shortcuts import render
from contacts.models import Contacts


def contacts(request):
    try:
        object = Contacts.objects.get()
    except Contacts.DoesNotExist:
        raise Http404

    response = render(
        request,
        'contacts/index.html',
        {'object': object, }
    )
    return response
