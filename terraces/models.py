from solo.models import SingletonModel
from common.models import PageDescription, PageHWAW, PagePortfolio, SimplePage


class Terrace(SimplePage, PageDescription, PagePortfolio, PageHWAW, SingletonModel):
    upload_to_dir = 'terraces'
    class Meta:
        verbose_name = 'терраса'
        verbose_name_plural = 'террасы'
