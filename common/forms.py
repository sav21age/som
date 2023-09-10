from django import forms
from django.forms import Textarea
# from codemirror import CodeMirrorTextarea
# from common.models import PageDescription, SimplePage
from common.models import SimplePage


# codemirror_widget = CodeMirrorTextarea(
#     mode="markdown",
#     # theme="eclipse",
#     # theme="neo",
#     config={
#         'fixedGutter': True,
#         'lineWrapping': True,
#         'matchBrackets': True,
#     },
# )


# class PageDescriptionAdminForm(forms.ModelForm):
#     # description_text = forms.CharField(label='Текст', required=False, widget=codemirror_widget)

#     class Meta:
#         model = PageDescription
#         widgets = {
#             'description_text': codemirror_widget,
#         }
#         exclude = []


class SimplePageAdminForm(forms.ModelForm):
    class Meta:
        model = SimplePage
        widgets = {
            'meta_description': Textarea(
                attrs={'rows': 3, 'style': 'width: 70%; font-size: 115%;'}),
        }
        exclude = []
