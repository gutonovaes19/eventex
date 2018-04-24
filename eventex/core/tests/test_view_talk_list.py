from django.test import  TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Talk, Speaker


class TalkListGet(TestCase):

    def setUp(self):
        #response = self.client.get('/palestras/')
        #aplicando o resolve_url, a linha de cima reescrita assim
        t1 = Talk.objects.create(title='Título da Palestra',
                            start='10:00',
                            description='Descrição da palestra.')
        t2 = Talk.objects.create(title='Título da Palestra',
                            start='13:00',
                            description='Descrição da palestra.')
        speaker = Speaker.objects.create(name='Henrique Bastos',
                                         slug='henrique-bastos',
                                         website='http://henriquebastos.net')
        #esse metodo ADD irá associar na relação many-to-many
        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code )

    def test_template(self):
        self.assertTemplateUsed(self.resp,'core/talk_list.html')

    def test_html(self):
        contents = [
            (2,'Título da Palestra'),
            (1,'10:00'),
            (1,'13:00'),
            (2,'/palestrantes/henrique-bastos/'),
            (2,'Descrição da palestra'),
        ]
        for count, expected in contents:
                with self.subTest():
                    self.assertContains(self.resp,expected,count)

    def test_context(self):
        """ aproximar o modelo do template. Mapear teste garantir que contexto tenha recursos\
         que preciamos"""
        variables = ['morning_talks', 'afternoon_talks']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)

