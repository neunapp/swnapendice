from django.http import Http404

from applications.home.models import Home


# context procesor para devover servicios de tipo classic tour
def home_banner(request):
    queryset = Home.objects.all().order_by('-created')[0]
    return {'home_banner':queryset}
