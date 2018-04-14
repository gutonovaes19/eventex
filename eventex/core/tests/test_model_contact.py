from django.core.exceptions import ValidationError
from django.test import  TestCase
from eventex.core.models import Speaker, Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb.pic'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,kind=Contact.cEMAIL,
                                         value='henrique@bastos.net')
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,kind=Contact.cPHONE,
                                        value='21-996186180')
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """contact kin should be limited to E or P"""
        contact = Contact(speaker=self.speaker,kind='A',value='B')
        self.assertRaises(ValidationError,contact.full_clean)

    def teste_str(self):
        #só instancia o objeto, nao cria no banco.
        contact = Contact(speaker=self.speaker, kind=Contact.cEMAIL,value='henrique@bastos.net')
        self.assertEqual('henrique@bastos.net', str(contact))

