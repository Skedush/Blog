"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .utils.responseAuthenticationRule import MyTokenObtainPairView


scheme_view = get_schema_view(
    openapi.Info(
        title='Blog API',
        default_version='v0.1',
        description='博客系统API接口文档',
        contact=openapi.Contact(email="candycakechocolate@hotmail.com"),
        license=openapi.License(name="Blog License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('', include('Blog.apps.article.urls')),
    path('', include('Blog.apps.user.urls')),
    # django后台管理路由页面
    path(r"admin/", admin.site.urls),
    # token相关
    path(r'api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # 接口文档相关
    path(r'api_doc/', scheme_view.with_ui('swagger',
         cache_timeout=0), name='Blog API'),
    path(r'api_redoc/', scheme_view.with_ui('redoc',
         cache_timeout=0), name='Blog API')
]
