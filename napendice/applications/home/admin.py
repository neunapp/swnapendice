# # django
from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Home
#
# # local
# from .models import Contact
#
# # Register your models here.
#
# # admin.site.register(Contact)
#
AdminSite.site_header = 'Adminstrador Apendice'
AdminSite.site_title = 'Apendice admin'

admin.site.register(Home)