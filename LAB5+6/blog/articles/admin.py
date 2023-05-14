from django.contrib import admin
from .models import Article
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')

admin.site.register(Article, ArticleAdmin)
