from django.contrib import admin
from django.urls import path, include
from api_sfn.views import ArticlesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
