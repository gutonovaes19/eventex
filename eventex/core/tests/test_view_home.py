from django.test import TestCase
from django.shortcuts import resolve_url as r

#testcase já vem com o django

class HomeTest(TestCase):
    def setUp(self):
        #self é uma variável de instancia para ficar visivel ns outras funcoes
        self.response = self.client.get(r('home'))

    def test_get(self):
        #Docstring - mensagem que erá retornada pelo teste
        """get / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use Index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)
