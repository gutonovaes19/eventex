# request - é o que foi enviado
# response, é o que tem que ser devolvido - chamou formulario, devolveu formulario
from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

def new(request):
    if request.method == 'POST':
        return create(request)
    return empty_form(request)

def empty_form(request):
    """ possibilita """
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})

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
               {'subscription': subscription}) #dicionario
    #/inscricao/1/ foi trocado para sunscriptions.pk. Pois o nro 1 é referencia ao PK.
    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))




def detail(request, pk):
    try:
        #1o pk é o kwargs do metodo Get. 2o pk é a variável que foi passada.
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404



    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})



#UNDESCORE - sinaliza aos programadores que posso mudar a API a qq momento, sem compromisso
def _send_mail(subject,  from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_,[from_, to])