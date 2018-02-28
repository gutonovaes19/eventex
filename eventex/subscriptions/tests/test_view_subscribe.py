#M2A12 PASSO2 - CRIAR A TESTE. CRIAR CENARIO DE
#PASSO7 - refatorar, trocar Foi cquando criou o setUp - Os testes estavam repetindo o comando RESPONSE.
#         criou a funcao setUp, trocou self.response por self.res

from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):
    def setUp(self):
        """GET /INSCRICAO/ MUST RETURN STATUS CODE 200 """
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200,self.resp.status_code) #PASSO3 - FOI AO TEMINAL E RODOU MANAGE TEST PARA TESTAR, PRECISOU IR AO YRL.PY

    def test_template(self):  #template é o formulario, a tela
        """Must use subscriptions/subscription_form.html """
        self.assertTemplateUsed(self.resp,'subscriptions/subscription_form.html')

    def test_html(self): #passo8- teste de aceitação, faciliatr a conexão com o que acontecerá com o HTML
        #o form html ainda nao existe, mas crio o teste do que deverá conter
        """ Html must contain input tags """
        tags = (('<form',1),
                ('<input',6),
                ('type="text"',3),
                ('type="email"',1),
                ('type="submit"',1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp,text,count)

    def test_csrf(self):
        """html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have SubscriptionForm"""
        # 25:00  tempplates são rendereizados versus rendereizado explicação????

        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
                    email='henrique@bastos.net', phone='21-996186180')
        self.resp  = self.client.post('/inscricao/', data)
    def test_post(self):
        """ Valid POST should edirect to /incricao/1/ """
        self.assertRedirects(self.resp,'/inscricao/1/')

    def test_send_subscribe_email(self):
        self.assertEqual(1,len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})  # a chaves indica que esta recebendo um dicionario do formulario

    def test_post(self):
        """Invalid POST should not redirect"""
        response = self.client.post('/inscricao/',{}) #a chaves indica que esta recebendo um dicionario do formulario
        self.assertEqual(200,self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form,SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())








