# django
from django.conf.urls import include, url

# local
from . import views

app_name="articulo_app"

urlpatterns = [

    # urls para la aplicacion articulo
    url(
        r'^ultimas-noticias-peru/$',
        views.ArticleListView.as_view(),
        name='article-list'
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
