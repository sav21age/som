from django.db import models
from solo.models import SingletonModel
from common.models import PageDescription, PageHWAW, PagePortfolio, PageRailings, SimplePage


class TerraceTypicalProject(models.Model):
    name = models.CharField('название', max_length=250)
    height = models.DecimalField('высота, м', max_digits=2, decimal_places=1, null=True)
    width = models.DecimalField('ширина, м', max_digits=3, decimal_places=1, null=True)
    length = models.DecimalField('длина, м', max_digits=3, decimal_places=1, null=True)
    
    frame_material = models.CharField('материал каркаса', max_length=250)
    # frame_length = models.PositiveSmallIntegerField('длина, мм',)
    frame_width = models.PositiveSmallIntegerField('ширина каркаса, мм', null=True)
    frame_thickness = models.PositiveSmallIntegerField('толщина каркаса, мм', null=True)

    coloring = models.CharField('окраска', max_length=250)

    flooring_material = models.CharField('материал настила', max_length=250)

    extra = models.CharField('дополнительно', max_length=250, blank=True)

    def __str__(self):
        return '{}'.format(self.name)
    
    class Meta:
        verbose_name = 'типовой проект'
        verbose_name_plural = 'типовой проект'


class Terrace(SimplePage, PageDescription, PagePortfolio, PageHWAW, PageRailings, SingletonModel):
    typical_project = models.ForeignKey(TerraceTypicalProject, verbose_name='типовой проект', blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'терраса'
        verbose_name_plural = 'террасы'
