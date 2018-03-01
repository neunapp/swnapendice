#
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #urls para miscelanea
    url(r'^', include('applications.miscelanea.urls')),
    # urls para la aplicacion home
    url(r'^', include('applications.home.urls')),
    # urls para la aplicacion articulo
    url(r'^', include('applications.articulo.urls')),
    #
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
