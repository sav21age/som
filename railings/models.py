from common.models import PageDescription, PageMenu, PagePortfolio, SimplePage


class Railing(SimplePage, PageDescription, PageMenu, PagePortfolio):
    class Meta:
        ordering = ('menu_order', )
        verbose_name = 'ограждение'
        verbose_name_plural = 'ограждения'
