# -*- coding: utf-8 -*-
# django
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# local
from .models import Contact
from .forms import ContactForm, SearchForm
from applications.articulo.models import Article

#
from applications.mixins import UpdateArticlesMixin
# Create your views here.


class ContactCreateView(UpdateArticlesMixin, CreateView):
    '''
    formulario de contactenos
    '''
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact/index.html'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            contact = form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class IndexView(UpdateArticlesMixin, TemplateView):
    '''
    Pagina principal de apendice donde se van a mostrar las noticias mas
    importantes del dia
    '''

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['portada'] = Article.objects.portada()
        context['destacados'] = Article.objects.outstanding()
        context['standar'] = Article.objects.standar()
        #
        context['form'] = SearchForm
        return context

    template_name = 'home/index.html'


class ArticleListView(UpdateArticlesMixin, ListView):
    context_object_name = 'articles'
    model = Article
    template_name = 'home/search.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        context['standar'] = Article.objects.standar()
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        queryset = Article.objects.search_article(q)
        return queryset
