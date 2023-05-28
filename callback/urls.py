from django.urls import path
from callback.views import callback_form

urlpatterns = [
    path('request/', callback_form, name='request'),
]
