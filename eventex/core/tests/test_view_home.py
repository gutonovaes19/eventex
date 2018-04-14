from django.test import TestCase
from django.shortcuts import resolve_url as r

#testcase já vem com o django

class HomeTest(TestCase):
    fixtures = ['keynotes.json']
    def setUp(self):
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

    def test_speakers(self):
        """ must show keynote speakers"""

        contents = [
            'href="{}"'.format(r('speaker_detail',slug='grace-hopper')),
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response,expected)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)



