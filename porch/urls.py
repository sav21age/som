from django.urls import path
from porch.views import porch

urlpatterns = [
    path('<slug:slug>/', porch, name='detail'),
]
