# django
from django.contrib import admin

# local
from .models import Category, Tag, Medios

# Register your models here.

class MediosAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'files',
        'files_url',
        'pk',
    )
    search_fields = ('name',)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Medios, MediosAdmin)
