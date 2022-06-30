from django.contrib import admin

from api_sfn.models import Article,CronJob

class Articles(admin.ModelAdmin):
    list_display= ('id','title','url','imageUrl','newsSite','summary','publishedAt','updatedAt','featured')
    list_display_links = ('title','summary','newsSite','url','imageUrl','featured','publishedAt')
    search_fields = ('title','id')

class CronJobs(admin.ModelAdmin):
    list_display= ('id','quantity','runAt')
    search_fields = ('runAt','id')

admin.site.register(Article, Articles)
admin.site.register(CronJob, CronJobs)