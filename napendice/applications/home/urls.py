# django
from django.conf.urls import include, url

# local
from . import views

app_name="home_app"

urlpatterns = [
    # urls para la aplicacion home
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    url(
        r'^buscar-noticias/$',
        views.ArticleListView.as_view(),
        name='buscar'
    ),
]
