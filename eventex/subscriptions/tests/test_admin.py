from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin
from eventex.subscriptions.dadosHb import dataHb

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

        #Subscription.objects.create(name=dataHb.name,
        ##                            cpf=dataHb.cpf,
         #                           email=dataHb.email,
         #                           phone=dataHb.phone)
        #utra sintaxe, usando dicionátio, sugerida pelo regis.santos wttd
        Subscription.objects.create(**dataHb)







