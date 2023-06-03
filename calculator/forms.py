from django import forms
from calculator.models import Coeff, CoeffStaircaseType, RailingType, Service, StepsMaterialType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML


class CalculatorForm(forms.Form):
    h = forms.IntegerField(
        label='Высота лестницы, м:',
        widget=forms.NumberInput(
            attrs={
                'type': 'range',
                # 'class': 'form-range',
                'value': 3,
                'min': 1,
                'max': 4,
                'step': 1,
            }
        ),
        required=False,
    )
    
    obj=Coeff.objects.filter(id=1).get()
    h_coeff = forms.IntegerField(
        widget=forms.HiddenInput(
            attrs={
                'value': obj.h,
            },
        ),
    )

    # obj=CoeffStaircaseType.is_visible_objects.filter(id=1).get()
    # cst_coeff = forms.IntegerField(
    #     widget=forms.HiddenInput(
    #         attrs={
    #             'value': obj.price,
    #         },
    #     ),
    # )

    cst_coeff = forms.ModelChoiceField(
        widget=forms.RadioSelect(),
        queryset=CoeffStaircaseType.is_visible_objects,
        to_field_name="price",
        label='Тип лестницы:',
        # initial=0,
        required=False,
    )


    st = forms.ModelChoiceField(
        widget=forms.RadioSelect(),
        queryset=StepsMaterialType.is_visible_objects,
        to_field_name="price",
        label='Тип материала ступеней:',
        # initial=0,
        required=False,
    )

    rt = forms.ModelChoiceField(
        widget=forms.RadioSelect(),
        queryset=RailingType.is_visible_objects,
        to_field_name="price",
        label='Тип ограждений:',
        # initial=0,
        required=False,
    )

    s = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        queryset=Service.is_visible_objects,
        to_field_name="price",
        label='Услуги:',
        # initial=[1, 2],
        required=False,
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["st"].initial = StepsMaterialType.is_visible_objects.first()
        self.fields["rt"].initial = RailingType.is_visible_objects.first()
        self.fields["cst_coeff"].initial = CoeffStaircaseType.is_visible_objects.first()
        self.fields["s"].initial = list(Service.is_visible_objects.only('id'))
        # self.fields["service"].label_from_instance = lambda item: f"{item} ({item.price} €)"

        self.helper = FormHelper()
        self.helper.form_id = 'form_calculator'
        self.helper.layout = Layout(
            Field('h_coeff'),
            Div(
                Div(
                    Field('h', template="calculator/slider.html"),
                    css_class='col-12 mb-3'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    Field('cst_coeff'),
                    css_class='col-12 col-sm-6'
                ),
                Div(
                    Field('st'),
                    css_class='col-12 col-sm-6'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    Field('rt'),
                    css_class='col-12 col-sm-6'
                ),
                Div(
                    Field('s'),
                    css_class='col-12 col-md-3'
                ),
                css_class='row'
            ),
            Div(
                HTML('<hr>'),
                Div(
                    # HTML('<span class="fw-bold">Металлокаркас:</span>'),
                    HTML('<span>Металлокаркас:</span>'),
                    css_class='col-6'
                ),
                Div(
                    # HTML('<span id="id_mf_amount" class="fw-bold"></span>&nbsp;<span class="fw-bold">руб.</span>'),
                    HTML('<span id="id_mf_amount"></span>'),
                    css_class='col-6 text-end'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    HTML('<span>Ступени:</span>'),
                    css_class='col-6'
                ),
                Div(
                    HTML('<span id="id_st_amount">'),
                    css_class='col-6 text-end'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    HTML('<span>Ограждения:</span>'),
                    css_class='col-6'
                ),
                Div(
                    HTML('<span id="id_rt_amount"></span>'),
                    css_class='col-6 text-end'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    HTML('<span>Услуги:</span>'),
                    css_class='col-6'
                ),
                Div(
                    HTML('<span id="id_s_amount">'),
                    css_class='col-6 text-end'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    HTML('<span class="fw-bold">Итого:</span>'),
                    css_class='col-6'
                ),
                Div(
                    HTML('<span id="id_total_amount" class="fw-bold"></span>'),
                    css_class='col-6 text-end'
                ),
                css_class='row mt-2'
            ),
        )


# class CalculatorForm(forms.Form):
#     h = forms.IntegerField(
#         label='Высота лестницы, м:',
#         widget=forms.NumberInput(
#             attrs={
#                 'type': 'range',
#                 # 'class': 'form-range',
#                 'value': 3,
#                 'min': 1,
#                 'max': 4,
#                 'step': 1,
#             }
#         ),
#         required=False,
#     )
    
#     obj=Coeff.objects.filter(id=1).get()
#     h_coeff = forms.IntegerField(
#         widget=forms.HiddenInput(
#             attrs={
#                 'value': obj.h,
#             },
#         ),
#     )

#     # obj=CoeffStaircaseType.is_visible_objects.filter(id=1).get()
#     # cst_coeff = forms.IntegerField(
#     #     widget=forms.HiddenInput(
#     #         attrs={
#     #             'value': obj.price,
#     #         },
#     #     ),
#     # )

#     st = forms.ModelChoiceField(
#         widget=forms.RadioSelect(),
#         queryset=StepsMaterialType.is_visible_objects,
#         to_field_name="price",
#         label='Тип материала ступеней:',
#         # initial=0,
#         required=False,
#     )

#     rt = forms.ModelChoiceField(
#         widget=forms.RadioSelect(),
#         queryset=RailingType.is_visible_objects,
#         to_field_name="price",
#         label='Тип ограждений:',
#         # initial=0,
#         required=False,
#     )

#     s = forms.ModelMultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple(),
#         queryset=Service.is_visible_objects,
#         to_field_name="price",
#         label='Услуги:',
#         # initial=[1, 2],
#         required=False,
#     )
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["st"].initial = StepsMaterialType.is_visible_objects.first()
#         self.fields["rt"].initial = RailingType.is_visible_objects.first()
#         self.fields["s"].initial = list(Service.is_visible_objects.only('id'))
#         # self.fields["service"].label_from_instance = lambda item: f"{item} ({item.price} €)"

#         self.helper = FormHelper()
#         self.helper.form_id = 'form_calculator'
#         self.helper.layout = Layout(
#             Field('h_coeff'),
#             Field('cst_coeff'),
#             Div(
#                 Div(
#                     Field('h', template="calculator/slider.html"),
#                     css_class='col-12 mb-3'
#                 ),
#                 css_class='row'
#             ),
#             Div(
#                 Div(
#                     Field('st'),
#                     css_class='col-12 col-sm-6'
#                 ),
#                 Div(
#                     Field('rt'),
#                     css_class='col-12 col-sm-6'
#                 ),
#                 css_class='row'
#             ),
#             Div(
#                 Div(
#                     Field('s'),
#                     css_class='col-12 col-md-3'
#                 ),
#                 css_class='row'
#             ),
#             Div(
#                 HTML('<hr>'),
#                 Div(
#                     # HTML('<span class="fw-bold">Металлокаркас:</span>'),
#                     HTML('<span>Металлокаркас:</span>'),
#                     css_class='col-6'
#                 ),
#                 Div(
#                     # HTML('<span id="id_mf_amount" class="fw-bold"></span>&nbsp;<span class="fw-bold">руб.</span>'),
#                     HTML('<span id="id_mf_amount"></span>'),
#                     css_class='col-6 text-end'
#                 ),
#                 css_class='row'
#             ),
#             Div(
#                 Div(
#                     HTML('<span>Ступени:</span>'),
#                     css_class='col-6'
#                 ),
#                 Div(
#                     HTML('<span id="id_st_amount">'),
#                     css_class='col-6 text-end'
#                 ),
#                 css_class='row'
#             ),
#             Div(
#                 Div(
#                     HTML('<span>Ограждения:</span>'),
#                     css_class='col-6'
#                 ),
#                 Div(
#                     HTML('<span id="id_rt_amount"></span>'),
#                     css_class='col-6 text-end'
#                 ),
#                 css_class='row'
#             ),
#             Div(
#                 Div(
#                     HTML('<span>Услуги:</span>'),
#                     css_class='col-6'
#                 ),
#                 Div(
#                     HTML('<span id="id_s_amount">'),
#                     css_class='col-6 text-end'
#                 ),
#                 css_class='row'
#             ),
#             Div(
#                 Div(
#                     HTML('<span class="fw-bold">Итого:</span>'),
#                     css_class='col-6'
#                 ),
#                 Div(
#                     HTML('<span id="id_total_amount" class="fw-bold"></span>'),
#                     css_class='col-6 text-end'
#                 ),
#                 css_class='row mt-2'
#             ),
#         )


# class CalculatorSForm(CalculatorForm):
#     obj=CoeffStaircaseType.is_visible_objects.filter(id=1).get()
#     cst_coeff = forms.IntegerField(
#         widget=forms.HiddenInput(
#             attrs={
#                 'value': obj.price,
#             },
#         ),
#     )


# class CalculatorGForm(CalculatorForm):
#     obj=CoeffStaircaseType.is_visible_objects.filter(id=2).get()
#     cst_coeff = forms.IntegerField(
#         widget=forms.HiddenInput(
#             attrs={
#                 'value': obj.price,
#             },
#         ),
#     )

# class CalculatorPForm(CalculatorForm):
#     obj=CoeffStaircaseType.is_visible_objects.filter(id=3).get()
#     cst_coeff = forms.IntegerField(
#         widget=forms.HiddenInput(
#             attrs={
#                 'value': obj.price,
#             },
#         ),
#     )

