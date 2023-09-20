from django.db import models
from treebeard.mp_tree import MP_Node


class Menu(MP_Node):
    name = models.CharField('название', max_length=30)
    url = models.CharField('url-адрес страницы', max_length=100, blank=True)
    is_visible = models.BooleanField('показывать?', default=1)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'
