from rest_framework.permissions import AllowAny, IsAuthenticated
from Blog.utils.customViewSet import CustomViewSet
from .serializers import UserInfoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserInfo
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render

# Create your views here.


class UserInfoViewset(CustomViewSet):
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [IsAuthenticated],
                                    'update': [IsAuthenticated],
                                    'retrieve': [AllowAny],
                                    'destroy': [IsAuthenticated]
                                    }
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user']

    # 根据action获取权限
    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]
