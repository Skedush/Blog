'''
自己定义一个ViewSet继承DRF的ModalViewSet
'''
from rest_framework.viewsets import ModelViewSet
from rest_framework import status,  generics
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenViewBase
from .response import CustomResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CustomViewSet(ModelViewSet):
    queryset = None
    serializer_class = None
    permission_classes = []
    search_fields = []
    filterset_fields = []
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    def initialize_request(self, request, *args, **kwargs):
        """
            Set the `.action` attribute on the view, depending on the request method.
            """
        request = super().initialize_request(request, *args, **kwargs)
        method = request.method.lower()
        if method == 'options':
            # This is a special case as we always provide handling for the
            # options method in the base `View` class.
            # Unlike the other explicitly defined actions, 'metadata' is implicit.
            self.action = 'metadata'
        else:
            self.action = self.action_map.get(method)
        return request

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return CustomResponse(data=serializer.data, code=201, success=True, msg="创建成功", status=status.HTTP_201_CREATED, headers=headers)

    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # return self.get_paginated_response(serializer.data)
            return CustomResponse(data=self.get_paginated_response(serializer.data), code=200, msg="success", success=True,  status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)
        return CustomResponse(data=serializer.data, code=200, msg="success", success=True,  status=status.HTTP_200_OK)

    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return CustomResponse(data=serializer.data, code=200, msg="success", success=True,  status=status.HTTP_200_OK)

    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return CustomResponse(data=serializer.data, code=200, msg="更新成功", success=True,  status=status.HTTP_200_OK)

    # 重构destroy方法

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # 当有is_deleted字段时修改为false，无时删除数据库条目
        if(instance.is_delete != None):
            instance.is_delete = True
            self.perform_update(instance)
        else:
            self.perform_destroy(instance)
        return CustomResponse(data=[], code=204, msg="删除成功", success=True,  status=status.HTTP_204_NO_CONTENT)


class CustomListAPIView(generics.ListAPIView):
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return CustomResponse(data=self.get_paginated_response(serializer.data), code=200, msg="success", success=True,  status=status.HTTP_200_OK)
        serializer = self.get_serializer(queryset, many=True)
        return CustomResponse(data=serializer.data, code=200, msg="success", success=True,  status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = serializers.TokenObtainPairSerializer

    # 重写post方法
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return CustomResponse(data=serializer.validated_data, status=status.HTTP_200_OK, code=200, msg="success", success=True,)
