from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # 使用DRF
    'django_filters',

    'drf_yasg',    # 使用yasg接口文档

    'Blog.apps.article',
    'Blog.apps.user',
    'Blog.apps.visitorfc',
]
SIMPLEUI_DEFAULT_THEME = 'ant.design.css'  # 后台管理皮肤，可以去官方选择
