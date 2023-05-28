from django.contrib import admin
from blocks.forms import BlockSVGAdminForm, BlockPriceAdminForm
from blocks.models import BlockSVG, BlockText, BlockPrice
from django.db import models
from django.forms import TextInput, Textarea


formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'style': 'width: 70%; font-size: 115%;'})},
    models.TextField: {'widget': Textarea(attrs={'rows': 7, 'style': 'width: 70%; font-size: 115%;'})},
}

class BlockSVGAdmin(admin.ModelAdmin):
    fields = ('block_name', 'title', 'description',
              'svg_path', 'order_number', 'is_visible',)
    list_display = ('title', 'order_number', 'block_name', )
    list_filter = ('is_visible', 'block_name', )
    form = BlockSVGAdminForm
    formfield_overrides = formfield_overrides

    # def has_module_permission(self, request):  # hide form dashboard
    #     return False

    # def svg_path_tag(self, obj):
    #     return mark_safe('<div style="background-color: rgb(121,174,200);"><img src="{url}" width="{width}" height="{height}" /></div>'.format(
    #         url=obj.svg_path.url,
    #         width=64,
    #         height=64,
    #     )
    # )

admin.site.register(BlockSVG, BlockSVGAdmin)


# class BlockTextAdmin(admin.ModelAdmin):
#     list_filter = ('is_visible', )
#     formfield_overrides = formfield_overrides

# admin.site.register(BlockText, BlockTextAdmin)


class BlockPriceAdmin(admin.ModelAdmin):
    list_filter = ('is_visible', )
    fields = ('title', 'img_path', 'price', 'is_visible', )
    list_display = ('title', 'price', )
    form = BlockPriceAdminForm
    formfield_overrides = formfield_overrides

admin.site.register(BlockPrice, BlockPriceAdmin)
