from django.contrib import admin
from .models import Article, Article_Tag, Article_genre


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time')


# Register your models here.
admin.site.register(Article,ArticleAdmin,)
admin.site.register(Article_Tag)
admin.site.register(Article_genre)
