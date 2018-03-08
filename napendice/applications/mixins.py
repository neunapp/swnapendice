# -*- coding: utf-8 -*-
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from applications.articulo.models import Article
from datetime import timedelta, datetime
from django.utils import timezone


#
class UpdateArticlesMixin(object):
    """ mixin para actualizar articulos programados"""

    def dispatch(self, request, *args, **kwargs):
        # recuperamos los articulos programados
        articulos = Article.objects.filter(
            published=False,
            programado=True,
        )
        #actualizamos los valores de cada articulo
        now_aware = timezone.now()
        #
        for a in articulos:
            if a.date <= now_aware:
                a.published=True
                a.save()
                print('se actualizo a publicado')
            else:
                print('**********')
        #
        return super(UpdateArticlesMixin, self).dispatch(request, *args, **kwargs)
