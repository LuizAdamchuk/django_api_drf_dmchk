from django import views
from django.contrib import admin
from django.urls import path, include
from api_sfn.views import ArticlesViewSet, home, post
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/pagination/<int:start>', home),
    path('blog/', home),
    path('posts/<int:site_id>', post),
    path('', include(router.urls))
]
