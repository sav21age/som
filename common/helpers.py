import os
import re
import uuid
import random
from django.forms import NumberInput, TextInput, Textarea
from django.db import models

# def get_image_path(instance, filename):
#     f = os.path.splitext(filename)
#     return '{0}-{1}{2}'.format(f[0], random.randint(10000, 99999), f[1])

quote = re.compile(r'\"(.*?)\"')
quote_office = re.compile(r'\“(.*?)\”')

formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'style': 'width: 70%; font-size: 115%;'})},
    models.TextField: {'widget': Textarea(attrs={'rows': 30, 'style': 'width: 70%; font-size: 115%;'})},
    models.IntegerField: {'widget': NumberInput(attrs={'style': 'width: 100px; font-size: 115%;'})},
    models.DecimalField: {'widget': NumberInput(attrs={'style': 'width: 100px; font-size: 115%;'})},
}

#--

def get_svg_path(instance, filename):
    f = os.path.splitext(filename)
    return "svg/%s-%s.svg" % (f[0], random.randint(10000, 99999))

def get_image_path(instance, filename):
    f = os.path.splitext(filename)
    dir = 'images'
    if hasattr(instance, 'upload_to_dir'):
        dir = '{0}/{1}'.format(dir, instance.upload_to_dir)
    return '{0}/{1}{2}'.format(dir, uuid.uuid1().hex, f[1].lower())
