from django import forms
from blocks.models import BlockImage, BlockSVG, BlockPrice
from blocks.widgets import SVGAdminWidget, IMGAdminWidget


class BlockSVGAdminForm(forms.ModelForm):
    class Meta:
        model = BlockSVG
        exclude = []
        widgets = {
            'svg_path': SVGAdminWidget(),
        }


class BlockPriceAdminForm(forms.ModelForm):
    class Meta:
        model = BlockPrice
        exclude = []
        widgets = {
            'img_path': IMGAdminWidget(),
        }


class BlockImageAdminForm(forms.ModelForm):
    class Meta:
        model = BlockImage
        exclude = []
        widgets = {
            'img_path': IMGAdminWidget(),
        }
