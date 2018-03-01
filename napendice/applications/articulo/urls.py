# django
from django.conf.urls import include, url

# local
from . import views

app_name="articulo_app"

urlpatterns = [

    # urls para la aplicacion articulo
    url(
        r'^nueva-noticia/$',
        views.ArticleAddView.as_view(),
        name='article-add'
    ),
    url(
        r'^articulo-listar/(?P<pk>\d+)/$',
        views.ArticleListView.as_view(),
        name='article-list'
    ),
    url(
        r'^articulo-update/(?P<pk>\d+)/$',
        views.ArticleUpdateView.as_view(),
        name='article-update'
    ),
    url(
        r'^articulo-delete/(?P<pk>\d+)/$',
        views.ArticleDeleteView.as_view(),
        name='article-delete'
    ),
    url(
        r'^(?P<category>[-\w]+)/$',
        views.ArticleCategoryView.as_view(),
        name='article-category'
    ),
    url(
        r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.ArticleDetailView.as_view(),
        name='article-detail'
    ),

]
