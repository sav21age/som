from django.urls import reverse
from solo.models import SingletonModel
from common.models import PageDescription, PageHWAW, PagePortfolio, SimplePage


class Bridge(SimplePage, PageDescription, PagePortfolio, PageHWAW, SingletonModel):
    class Meta:
        verbose_name = 'мостик'
        verbose_name_plural = 'мостики'

    def get_absolute_url(self):
        return reverse('decorative-bridge')
