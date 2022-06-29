from django.contrib import admin

from api_sfn.models import Article

class Articles(admin.ModelAdmin):
    list_display= ('id','title','url','imageUrl','newsSite','summary','publishedAt','updatedAt','featured')
    list_display_links = ('title','summary','newsSite','url','imageUrl','featured','publishedAt')
    search_fields = ('title','id')

admin.site.register(Article, Articles)