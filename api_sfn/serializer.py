from rest_framework import serializers
from api_sfn.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['site_id','title','imageUrl','url','newsSite','summary','publishedAt','updatedAt','featured']


