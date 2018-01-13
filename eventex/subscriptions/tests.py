#M2A12 PASSO2 - CRIAR A TESTE. CRIAR CENARIO DE
#PASSO7 - refatorar, trocar Foi cquando criou o setUp - Os testes estavam repetindo o comando RESPONSE.
#         criou a funcao setUp, trocou self.response por self.res
from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        #cria instancia SELF para ficar visivel as outras funcoes
        """GET /INSCRICAO/ MUST RETURN STATUS CODE 200 """
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        #response = self.client.get() ---- essa linha virou test_get mais abaixo e foi trocada pela linha abaixo
        self.assertEqual(200,self.resp.status_code) #PASSO3 - FOI AO TEMINAL E RODOU MANAGE TEST PARA TESTAR, PRECISOU IR AO YRL.PY

    def test_template(self):  #template é o formulario, a tela
        """Must use subscriptions/subscription_form.html """
        #response = self.client.get() ---- essa linha virou test_get mais abaixo e foi trocada pela linha abaixo passo7
        #self.asertTemplateUsed(response,'subscriptions/subscription_form.html') --- substituida pela linha abaoxo paso7
        self.assertTemplateUsed(self.resp,'subscriptions/subscription_form.html')

    def test_html(self): #passo8- teste de aceitação, faciliatr a conexão com o que acontecerá com o HTML
        #o form html ainda nao existe, mas crio o teste do que deverá conter
        """ Html must contain input tags """
        self.assertContains(self.resp,'<form')
        self.assertContains(self.resp,'<input',6)   #eram 5, depois do CRFS que é hidden (django, oculto, para evitar
                                                    # invasores incluiu teste de 6 inputs
        self.assertContains(self.resp,'type="text"', 3)
        self.assertContains(self.resp,'type="email"')
        self.assertContains(self.resp,'type="submit"')

    def test_csrf(self):
        """html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have SubscriptionForm"""
        # 25:00  tempplates são rendereizados versus rendereizado explicação????
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """form must have 4 fields 29:00"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name','cpf','email','phone'], list(form.fields))

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
                    email='henrique@bastos.net', phone='21-99618-6180')
        self.resp  = self.client.post('/inscricao/', data)
    def test_post(self):
        """ Valid POST should edirect to /incricao/ """
        self.assertEqual(302,self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1,len(mail.outbox))

    def test_subscription_email_subject(self):
        email = mail.outbox[0] #outbox guarda uma lista [] de objetos enviados Objetos tem atributos como subject
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect,email.subject)

    def test_subscription_email_from(self):
        email = mail.outbox[0]  # outbox guarda uma lista [] de objetos enviados Objetos tem atributos como subject
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]  # outbox guarda uma lista [] de objetos enviados Objetos tem atributos como subject
        expect = ['contato@eventex.com.br','henrique@bastos.net']
        self.assertEqual(expect, email.to)

    def test_subscription_email_body(self):
        email = mail.outbox[0]  # outbox guarda uma lista [] de objetos enviados Objetos tem atributos como subject

        self.assertIn('Henrique Bastos',email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('henrique@bastos.net', email.body)
        self.assertIn('21-99618-6180', email.body)

class SubscribeInvalidPost(TestCase):
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

class SubscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
                    email='henrique@bastos.net', phone='21-99618-6180')
        response = self.client.post('/inscricao/',data,follow=True)
        self.assertContains(response,'Inscrição realizada com sucesso!')








