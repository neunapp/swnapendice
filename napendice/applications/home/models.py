# future
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Contact(TimeStampedModel):
    """Django data model Contact"""

    name = models.CharField('nombre', blank=True, max_length=100)
    email = models.EmailField('email')
    telephone = models.CharField('telefono', blank=True, max_length=12)
    subject = models.CharField('asunto', max_length=50)
    send = models.CharField('consulta', max_length=150)

    class Meta:
        verbose_name = 'Tipo de Contacto'
        verbose_name_plural = 'Tipos de Contactos'

    def __str__(self):
        return self.name
