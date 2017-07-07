"""Toda viwe no Django recebe ao menos 1 argumento de http request, retorna sempre uma instancia de http response"""


from django.shortcuts import render


def subscribe(request):
    return render(request, 'subscriptions/subscription_form.html')
