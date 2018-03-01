# django
from django.conf.urls import include, url

# local
from . import views

app_name="miscelanea_app"

urlpatterns = [
    url(
        r'^lista-categorias/$',
        views.ListaCategoriasView.as_view(),
        name='category-list'
    ),
]
