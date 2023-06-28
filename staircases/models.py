from django.db import models
from blocks.models import BlockPrice, BlockSVG
from common.models import PageCalculator, PageDescription, PageHWAW, PageMenu, PagePortfolio, PageRailings, SimplePage, TypicalProject


class StaircaseTypicalProject(TypicalProject):
    frame_broken_material = models.CharField('материал "ломаного" каркаса', max_length=250, blank=True)
    frame_broken_width = models.PositiveSmallIntegerField('ширина "ломаного" каркаса, мм', blank=True, null=True)
    frame_broken_thickness = models.PositiveSmallIntegerField('толщина "ломаного" каркаса, мм', blank=True, null=True)

    frame_straight_material = models.CharField('материал "прямого" каркаса', max_length=250, blank=True)
    frame_straight_width = models.PositiveSmallIntegerField('ширина "прямого" каркаса, мм', blank=True, null=True)
    frame_straight_thickness = models.PositiveSmallIntegerField('толщина "прямого" каркаса, мм', blank=True, null=True)

    coloring = models.CharField('окраска', max_length=250)

    steps_material = models.CharField('материал ступеней', max_length=250)
    steps_height = models.DecimalField('высота ступеней, м', max_digits=4, decimal_places=2, blank=True, null=True)


class Staircase(SimplePage, PageCalculator, PageDescription, PageMenu, PagePortfolio, PageHWAW, PageRailings):
    block_svg_title = models.CharField(
        'заголовок', max_length=200, blank=True)
    block_svg = models.ManyToManyField(
        BlockSVG, verbose_name='объекты', related_name='block_svg',
        blank=True, db_index=True)

    block_price = models.ManyToManyField(
        BlockPrice, verbose_name='объекты', related_name='+',
        blank=True, db_index=True)

    typical_project = models.ForeignKey(
        StaircaseTypicalProject, verbose_name='типовой проект', 
        blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('menu_order', )
        verbose_name = 'лестницу'
        verbose_name_plural = 'лестницы'
