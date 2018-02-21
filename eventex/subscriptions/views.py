"""Toda viwe no Django recebe ao menos 1 argumento de http request, retorna sempre uma instancia de http response"""
# M2A12 passo5

# request - é o que foi enviado
# response, é o que tem que ser devolvido - chamou formulario, devolveu formulario
from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    """ cria a subsinscricao  """
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        """ aborta e exibe formulario com erro """
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})
    # sendmail
    _send_mail('Confirmação de Inscrição',
               settings.DEFAULT_FROM_EMAIL,
               form.cleaned_data['email'],
               'subscriptions/subscription_email.txt',
               form.cleaned_data)

    Subscription.objects.create(**form.cleaned_data)

    messages.success(request,'Inscrição realizada com sucesso!')
    return HttpResponseRedirect('/inscricao/')


def new(request):
    """ possibilita """
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})
#UNDESCORE - sinaliza aos programadores que posso mudar a API a qq momento, sem compromisso
def _send_mail(subject,  from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_,[from_, to])