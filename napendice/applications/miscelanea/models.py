# future
from __future__ import unicode_literals
import os

# third-party
from model_utils.models import TimeStampedModel

# django
from django.db import models
from django.contrib.auth.models import User

#manager
from .managers import CategoryManager

# Create your models here.

class Category(TimeStampedModel):
    '''
    modelo para almacenar categorias
    '''
    name = models.CharField('nombre', max_length=150)
    anulate = models.BooleanField(default=False)

    objects = CategoryManager()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    '''modelo djanog para etiquetas'''

    name = models.CharField('nombre', max_length=150)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Medios(TimeStampedModel):
    name = models.CharField(
        blank=True,
        max_length=100
    )
    files = models.FileField(
        upload_to='files',
        blank=True,
        null=True,
    )
    files_url = models.URLField(
        blank=True,
    )

    class Meta:
        verbose_name = 'Medio'
        verbose_name_plural = 'Medios'

    def delete(self,*args,**kwargs):
        if os.path.isfile(self.files.path):
            os.remove(self.files.path)

        super(Medios, self).delete(*args,**kwargs)

    def __str__(self):
        return str(self.files)
