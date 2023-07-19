from solo.admin import SingletonModelAdmin
from django.contrib import admin
from index.models import Index
from common.admin import PageCalculatorAdmin, PageDescriptionAdmin, PageHWAWAdmin, PagePortfolioAdmin, PagePriceAdmin, SimplePageAdmin


class IndexAdmin(SimplePageAdmin, PageCalculatorAdmin, PagePriceAdmin, PageHWAWAdmin, PagePortfolioAdmin, PageDescriptionAdmin, SingletonModelAdmin):
    filter_horizontal = ('hwaw', 'block_price', 'block_svg',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets + (
            ('О компании', {
                'fields': ('about_title', 'about_text',)
            }),
            ('Блок с векторной графикой', {
                'fields': ('block_svg_title', 'block_svg', )
            }),
            # ('Блок с ценами', {
            #     'fields': ('block_price',)
            # }),
        )

admin.site.register(Index, IndexAdmin)


# def get_fieldsets(self, request, obj=None):
#     fieldsets = super().get_fieldsets(request, obj)
#     lst = []
#     for t in fieldsets:
#         if t[0] != 'Меню':
#             lst.append(t)
#     return tuple(lst) + (
#         ('Блок с векторной графикой', {
#             'fields': ('block_svg_title', 'block_svg', )
#         }),
#         ('Блок с ценами', {
#             'fields': ('prices',)
#         }),
#         ('О компании', {
#             'fields': ('about_title', 'about_text',)
#         }),
#         ('Как мы работаем?', {
#             'fields': ('hwaw',)
#         }),
#         ('Наши работы', {
#             'fields': ('portfolio_title',)
#         }),
#     )
