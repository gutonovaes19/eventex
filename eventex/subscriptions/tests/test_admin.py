from unittest.mock import Mock

from django.test import TestCase

from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


#Proposta: criar uma classe onde preciso
# 1o existe uma ação instalada
# 2o Instanciar o ModelAdmin para realizar teste (TESTE UNITÁRIO) através dele, sem precisar saber da estrutura do mesmo
#    Não precisará do self. VER documenação do admin.site
#dadosHb = namedtuple('dadosHb', ('name', 'cpf', 'email', 'phone'))
#data = dadosHb(name='Henrique Bastos',
#               cpf='12345678901',
#               email='henrique@bastos.net',
#               phone='21 - 996186180'
#               )

class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Henrique Bastos', cpf='12345678901',
                                    email='henrique@bastos.net', phone='21 - 996186180'
                                    )
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """ Action mark as paid should be installed"""
        # par1 (modelo) par2 (instancia do admin site)
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """it should mark all selected subscriptions as paid"""
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """It Should send a message to the user """
        mock = self.call_action()
        mock.assert_called_once_with(None,'1 inscrição foi marcada como paga.')

    def call_action(self):
        queryset = Subscription.objects.all()
        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock
        self.model_admin.mark_as_paid(None, queryset)
        SubscriptionModelAdmin.message_user = old_message_user
        return mock










