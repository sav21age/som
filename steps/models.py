from common.models import PageDescription, PageMenu, PagePortfolio, SimplePage


class Steps(SimplePage, PageDescription, PageMenu, PagePortfolio):
    class Meta:
        ordering = ('menu_order', )
        verbose_name = 'ступень'
        verbose_name_plural = 'ступени'
