from django import forms
from django.forms import Textarea
from common.models import SimplePage

class SimplePageAdminForm(forms.ModelForm):
    class Meta:
        model = SimplePage
        widgets = {
            'meta_description': Textarea(attrs={'rows': 3, 'style': 'width: 70%; font-size: 115%;'}),
        }
        exclude = []