from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewset, MenuViewset, ArticleViewset

# ViewSet可以使用router拼接
router = DefaultRouter()
router.register(r'category', CategoryViewset)
router.register(r'article', ArticleViewset)

urlpatterns = [
    path('', include(router.urls)),
    # ListAPIView不是ViewSet视图,使用普通格式url
    path('menu/', MenuViewset.as_view()),
]
