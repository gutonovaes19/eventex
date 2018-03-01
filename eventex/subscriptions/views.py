# request - é o que foi enviado
# response, é o que tem que ser devolvido - chamou formulario, devolveu formulario
from django.conf import settings
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

    subscription = Subscription.objects.create(**form.cleaned_data)
    # send subscriptions email
    _send_mail('Confirmação de Inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})
    return HttpResponseRedirect('/inscricao/{}/'.format(subscription.pk))


def new(request):
    """ possibilita """
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


def detail(request, pk):
    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription':Subscription()})



#UNDESCORE - sinaliza aos programadores que posso mudar a API a qq momento, sem compromisso
def _send_mail(subject,  from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_,[from_, to])