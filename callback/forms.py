from django import forms


class CallbackForm(forms.Form):
    name = forms.CharField(
        max_length=50, label='Ваше имя', required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', }),)
    phone = forms.CharField(
        max_length=50, label='Ваш номер телефона', required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'data-phone-pattern': '',
        }),)
    recaptcha = forms.CharField(widget=forms.HiddenInput(
        attrs={'class': 'g-recaptcha-response', }
    ))
