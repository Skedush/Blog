from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserInfoViewset

# ViewSet可以使用router拼接
router = DefaultRouter()
router.register(r'user/info', UserInfoViewset)

urlpatterns = [
    path('', include(router.urls)),
]
