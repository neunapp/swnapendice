#django import
from django.conf import settings
from django.db import models


class CategoryManager(models.Manager):
    """procedimientos para tabla Categoria"""

    def listar_categoria(self):
        lista = self.all().order_by('name')

        return lista
