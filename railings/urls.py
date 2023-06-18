from django.urls import path
from railings.views import railings

urlpatterns = [
    path('<slug:slug>/', railings, name='detail'),
]
