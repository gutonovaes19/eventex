#m2a12 30:00
from django import forms
from django.core.exceptions import  ValidationError

def validate_cpf(value):
    #verifica se são só numeros
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF deve conter 11 números.', 'length')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
