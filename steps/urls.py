from django.urls import path
from steps.views import steps

urlpatterns = [
    path('<slug:slug>/', steps, name='detail'),
]
