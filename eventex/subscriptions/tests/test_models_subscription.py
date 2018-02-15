from django.test import TestCase
from eventex.subscriptions.models import Subscription


#1o cenario
class SubscriptionModelTest(TestCase):
    def test_create(selfs):
        obj = Subscription(
            name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-996186180'
        )
        obj.save()
        self.assertTrue(Subscriptions.objects.exists())
