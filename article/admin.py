from django.contrib import admin
from .models import Article

#To show as a Table in admin page
class ArticleAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'desc','author']
    list_display_links=['id', 'title']

# Register your models here.

admin.site.register(Article, ArticleAdmin)