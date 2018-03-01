# django
from django.contrib import admin

# local
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'date',
        'type_article',
        'published',
        'pk',
    )
    search_fields = ('title', 'description')
    list_filter = ('date',)
    fields = (
        'title',
        'category',
        'description',
        'type_article',
        'content',
        'credits_article',
        'city',
        'tag',
        'published',
        'show_home',
        'image',
        'credits_image',
    )
    filter_horizontal = ('tag',)


admin.site.register(Article,ArticleAdmin)
