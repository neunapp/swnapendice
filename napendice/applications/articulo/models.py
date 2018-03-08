# future
from __future__ import unicode_literals

# standard library
from datetime import timedelta, datetime

# third-party
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# django
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings

# local
from applications.miscelanea.models import Category, Tag
from .managers import ArticleManager

# Create your models here.


class Article(TimeStampedModel):
    """Django data model Articulos"""

    TYPE_STANDARD = 'S'  # ESTANDAR
    TYPE_FRONT = 'F'  # PORTADA
    TYPE_OUTSTANDING = 'O'  # DESTACADO
    TYPE_CHOICES = (
        (TYPE_STANDARD, 'Estandar'),
        (TYPE_FRONT, 'Portada'),
        (TYPE_OUTSTANDING, 'Destacado'),
    )
    category = models.ForeignKey(
        Category,
        verbose_name='categoria',
        on_delete=models.CASCADE,
    )
    title = models.CharField('titulo', max_length=200)
    description = models.TextField('descripcion')
    bajada = models.TextField('bajada', blank=True)
    date = models.DateTimeField('fecha de publicacion', blank=True, null=True)
    type_article = models.CharField(
        'tipo de articulo',
        max_length=2,
        choices=TYPE_CHOICES
    )
    city = models.CharField('ciudad', max_length=100)
    content = RichTextUploadingField('contenido')
    show_home = models.BooleanField('mostrar en home')
    views = models.PositiveIntegerField('vistas', default=0, editable=False)
    credits_article = models.CharField('creditos articulo', max_length=150)
    image = models.ImageField(upload_to='portada', verbose_name='imagen')
    credits_image = models.CharField('creditos imagen', max_length=150)
    slug = models.SlugField(editable=False, max_length=200)
    tag = models.ManyToManyField(Tag, verbose_name='tag')
    published = models.BooleanField('publicado', default=False)
    programado = models.BooleanField('programado', default=False)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="usuario_editor",
        verbose_name="Creado por",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    user_modified = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="usuario_editor_mod",
        verbose_name="Modificado por",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    objects = ArticleManager()

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(Article, self).save(*args, **kwargs)
