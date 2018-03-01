# -*- coding: utf-8 -*-

from django.db.models.manager import Manager


class ArticleManager(Manager):
    '''
    manager para el modelo articulo
    '''

    def portada(self):
        '''
        recuperar el articulo de la portada de acuerdo a la fecha
        '''
        portada = self.filter(
            published=True,
            type_article='F',
        ).order_by('-created')[0]
        return portada

    def outstanding(self):
        '''
        lista de los 3 primeros articulos destacados
        '''
        destacado = self.filter(
            published=True,
            type_article='O'
        ).order_by('-created')[:3]
        return destacado

    def standar(self):
        '''
        lista de las 8 primeros articulos de tipo standar
        '''
        standar = self.filter(
            published=True,
            type_article='S',
        ).order_by('-created')[:12]
        return standar

    def articleCategory(self, category):
        '''
        Lista de todos los articulos de acuerdo a una categoria.
        '''
        #correcion
        articles = self.filter(
            published=True,
            category__name=category
        ).order_by('type_article').order_by('-modified')[:20]
        return articles

    def article_recent(self):
        '''
        Lista de todos los articulos recientes.
        '''
        #correcion
        articles = self.filter(
            published=True,
        ).order_by('-created')[:7]
        return articles

    def search_article(self, kword):
        """buscamos articulo por palabra clave"""
        return self.filter(
            published=True,
            title__icontains=kword,
        ).order_by('-created')

    def article_by_state(self, kword):
        """recupera articulos segun estado"""
        if kword == '0':
            #publicados
            return self.filter(
                published=True,
            ).order_by('-created')[:100]

        elif kword == '1':
            #borrador
            return self.filter(
                published=False,
            ).order_by('-created')[:100]
        elif kword == '2':
            #todas
            return self.all().order_by('-created')[:15]
        else:
            #eliminados
            return self.all().order_by('-created')[:15]
