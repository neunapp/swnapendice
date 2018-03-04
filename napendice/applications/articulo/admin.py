# django
from django.contrib import admin

# local
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'type_article',
        'published',
        'user_created',
        'user_modified',
    )
    search_fields = ('title', 'description')
    list_filter = ('date',)
    fields = (
        'title',
        'category',
        'description',
        'bajada',
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
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user_created = request.user
        obj.user_modified = request.user
        obj.save()

admin.site.register(Article,ArticleAdmin)
