# -*- coding: utf-8 -*-
# django
from django.urls import reverse_lazy, reverse
from django.conf import settings
#
from django.views.generic import TemplateView, ListView, DeleteView
from django.views.generic.edit import CreateView

#import models
#from .models import Medios

#import forms
#from .forms import MediosForm


# class MediosCreateView(CreateView):
#     """Metodo para Guardar Medios"""
#
#     form_class = MediosForm
#     success_url = reverse_lazy('miscelanea_app:medios-list')
#     template_name = 'miscelanea/medios/add.html'
#
#     def form_valid(self, form):
#         medios = form.save(commit=False)
#         #recuperamos la url
#         medios.files_url = "http://apendice.pe"+medios.files.url
#         medios.save()
#
#         return super(MediosCreateView, self).form_valid(form)


# class MediosListView(ListView):
#     """Vista que lista los archivos Media"""
#
#     context_object_name = 'list_medios'
#     #model = Medios
#     template_name = 'miscelanea/medios/list.html'


# class MediosDeleteView(DeleteView):
#     model = Medios
#     success_url = reverse_lazy('miscelanea_app:medios-list')
#     template_name = 'miscelanea/medios/delete.html'



class ListaCategoriasView(TemplateView):
    template_name = 'miscelanea/list.html'
