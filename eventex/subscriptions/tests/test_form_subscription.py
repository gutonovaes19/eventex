from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
""" Teste unitário do/para o formulario """

class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        """form must have 4 fields 29:00"""
        expected = ['name','cpf','email','phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

