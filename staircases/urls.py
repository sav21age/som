from django.urls import path
from staircases.views import staircase

urlpatterns = [
    path('<slug:slug>/', staircase, name='detail'),
]
