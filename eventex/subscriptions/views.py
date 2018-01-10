"""Toda viwe no Django recebe ao menos 1 argumento de http request, retorna sempre uma instancia de http response"""
#M2A12 passo5

#request - é o que foi enviado
#response, é o que tem que ser devolvido - chamou formulario, devolveu formulario
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request): #Aula m2a12 - até 18 minutos #m2a12 passo6 toda funcao é um callabel
    #return httpresponse() - trocado pela linha abaixo durante os testes, passo a passo, foi criando cada linha
    #context = {'form':None}
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)
