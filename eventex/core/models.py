from django.db import models
from django.shortcuts import resolve_url as r

class Speaker(models.Model):
    name = models.CharField('nome',max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail',slug=self.slug)



class Contact(models.Model):
    #atributo de classe -
    #tupla de tuplas
    #o bloco será validado no full_clean, método da classe
    cEMAIL = 'E'
    cPHONE = 'P'

    KINDS = (
        (cEMAIL,'Email'),
        (cPHONE,'Telefone'),
    )
    #campos de realcionameno, o verbolsename vem no final
    speaker = models.ForeignKey('Speaker', verbose_name='palestante')
    kind = models.CharField(max_length=1, choices=KINDS)
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField('título',max_length=200)
    start = models.TimeField('início', blank=True, null=True)
    description = models.TextField('descrição', blank=True)
    speakers=models.ManyToManyField('Speaker',verbose_name = 'palestrantes', blank=True )

    class Meta:
        verbose_name_plural = 'palestras'
        verbose_name = 'palestra'

    def __str__(self):
        return self.title

