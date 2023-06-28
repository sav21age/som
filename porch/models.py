from django.db import models
from common.models import PageDescription, PageHWAW, PageMenu, PagePortfolio, PageRailings, SimplePage, TypicalProject


class PorchTypicalProject(TypicalProject):
    height = models.DecimalField('высота, м', max_digits=2, decimal_places=1, null=True)
    width = models.DecimalField('ширина, м', max_digits=2, decimal_places=1, null=True)
    # length = models.DecimalField('длина, м', max_digits=2, decimal_places=1, null=True)
    depth = models.DecimalField('глубина, м', max_digits=2, decimal_places=1, null=True)
    
    frame_kosour_count = models.PositiveSmallIntegerField('количество косоуров', null=True)
    frame_material = models.CharField('материал каркаса', max_length=250)
    frame_width = models.PositiveSmallIntegerField('ширина каркаса, мм', null=True)
    frame_thickness = models.PositiveSmallIntegerField('толщина каркаса, мм', null=True)

    coloring = models.CharField('окраска', max_length=250)

    steps_material = models.CharField('материал ступеней', max_length=250)
    steps_height = models.DecimalField('высота ступеней, м', max_digits=4, decimal_places=2, null=True)

    extra = models.CharField('дополнительно', max_length=250, blank=True)


class Porch(SimplePage, PageDescription, PageMenu, PagePortfolio, PageHWAW, PageRailings):
    typical_project = models.ForeignKey(PorchTypicalProject, verbose_name='типовой проект', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('menu_order', )
        verbose_name = 'крыльцо'
        verbose_name_plural = 'крыльцо'
