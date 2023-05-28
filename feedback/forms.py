from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class FeedbackForm(forms.Form):
    sender = forms.EmailField(max_length=50, label='E-mail', required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control',}),)
    subject = forms.CharField(max_length=100, label='Subject', required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control',}),)
    message = forms.CharField(label='Message', required=True,
                              widget=forms.Textarea(attrs={'class': 'form-control',}),)
    captcha = ReCaptchaField()
