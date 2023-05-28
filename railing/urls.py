from django.urls import path
from railing.views import railing

urlpatterns = [
    path('<slug:slug>/', railing, name='detail'),
]
