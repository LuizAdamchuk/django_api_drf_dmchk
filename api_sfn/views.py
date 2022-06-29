from rest_framework import viewsets
from api_sfn.models import Article
from api_sfn.serializer import ArticleSerializer

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        site_id = self.request.query_params.get('site_id', None)
        start = self.request.query_params.get('start', None)

        if site_id is not None:
            queryset = queryset.filter(site_id=site_id)
        elif start is not None:
            queryset = queryset.all()[int(start):int(start)+30]
        return queryset

