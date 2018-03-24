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

    def clean_name(self):
        name = self.cleaned_data['name']
        words = []
        #for w in name.split():
        #    words.append(w.capitalize())
        #expressao abaixo substitui o codigo acima
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

