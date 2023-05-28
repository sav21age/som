from django.conf.urls import url
from feedback.views import *

app_name='feedback'

urlpatterns = [
    url(r'^$', FeedbackFormView.as_view(), name='form'),
    url(r'^success/$', ThanksTemplateView.as_view(), name='success'),
    url(r'^failure/$', FailureTemplateView.as_view(), name='failure'),
]

