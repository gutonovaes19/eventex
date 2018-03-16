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
    def test_has_action(self):
        """ Action mark as paid should be installed"""
        # par1 (modelo) par2 (instancia do admin site)
        model_admin = SubscriptionModelAdmin(Subscription,admin.site)
        self.assertIn('mark_as_paid', model_admin.actions)

    def test_mark_all(self):
        """it should mar all selected subscriptions as paid"""
        Subscription.objects.create(name='Henrique Bastos',
                                    cpf='12345678901',
                                    email='henrique@bastos.net',
                                    phone='21 - 996186180'
                                    )
        queryset = Subscription.objects.all()
        #instancir o model_admin
        model_admin = SubscriptionModelAdmin(Subscription, admin.site)  # instanciei

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        #chamar ation
        model_admin.mark_as_paid(None,queryset)
        #verificar o resultato
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
        SubscriptionModelAdmin.message_user = old_message_user


    def test_message(self):
        """It Should send a message to the user """
        Subscription.objects.create(name='Henrique Bastos',
                                    cpf='12345678901',
                                    email='henrique@bastos.net',
                                    phone='21 - 996186180')

        model_admin = SubscriptionModelAdmin(Subscription, admin.site)
        queryset = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        model_admin.mark_as_paid(None, queryset)

        mock.assert_called_once_with(None,'1 inscrição foi marcada como paga.')

        SubscriptionModelAdmin.message_user = old_message_user









