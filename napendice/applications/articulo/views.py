# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# django
from django.views.generic import (
    DetailView,
    TemplateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# local
from applications.home.forms import SearchForm
from .models import Article
from .functions import update_type_article


class ArticleDetailView(DetailView):
    '''
    Vista para mostrar el detalle de un articulo.
    '''
    model = Article
    template_name = 'articulo/articulo.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['standar'] = Article.objects.standar()
        #noticias recientes
        context['recientes'] = Article.objects.article_recent()
        return context


class ArticleCategoryView(TemplateView):
    '''
    Vista para mostrar todos los articulos de acuerdo a las categorias.
    '''
    template_name = 'articulo/article_category.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleCategoryView, self).get_context_data(**kwargs)
        # recuperamos el valro q viene por url
        category = self.kwargs['category']
        if category == 'politica':
            category = 'política'

        if category == 'investigacion':
            category = 'investigación'

        if category == 'miscelanea':
            category = 'miscelánea'

        # lista de articulos de acuerdo a una categoria
        articles = Article.objects.articleCategory(category)
        # cantidad de articulos
        count = articles.count()
        context['count'] = count

        #contexto para formulario de busqeuda
        context['form'] = SearchForm

        # condiciones para mostrar contendio en la pagina y no renderize html
        if count >= 1:
            context['portada'] = articles[0]
        if count >= 2:
            context['destacados'] = articles[1:4]
        if count >= 5:
            context['standar'] = articles[4:]
        if count < 6:
            context['articles'] = Article.objects.outstanding()
        return context


class ArticleAddView(TemplateView):
    template_name = 'articulo/add.html'


class ArticleListView(TemplateView):
    """"vista que lista articulos por estado"""
    template_name = 'articulo/list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['kword'] = self.kwargs['pk']
        return context


class ArticleUpdateView(DetailView):
    """"vista para actualizar un articulo"""
    template_name = 'articulo/update.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        context['kword'] = self.kwargs['pk']
        return context


class ArticleDeleteView(DeleteView):
    """metodo para eliminar un articulo"""
    model = Article
    template_name = 'articulo/delete.html'
    success_url = reverse_lazy('articulo_app:article-list', kwargs = {'pk' : '0'})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        update_type_article('delete',self.object.type_article)
        self.object.delete()
        success_url = self.get_success_url()

        return HttpResponseRedirect(success_url)
