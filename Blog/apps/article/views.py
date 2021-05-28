from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from Blog.utils.customViewSet import CustomViewSet, CustomListAPIView
from .serializers import ArticleSerializer, CategorySerializer, MenuSerializer
from .models import Category, Article
from Blog.utils.drfPaginate import DrfPaginate
from rest_framework.permissions import IsAuthenticated, AllowAny


class CategoryViewset(CustomViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['parent', 'id']
    ordering_fields = ['sort', 'update_time', 'create_time']

    def get_queryset(self):
        # 只取没有删除的category
        return Category.objects.filter(is_delete=False)


class MenuViewset(CustomListAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['parent']
    ordering_fields = ['sort', 'update_time', 'create_time']

    # 获取菜单
    def get_queryset(self):
        # query_params = self.request.query_params
        # if(query_params and query_params.get('init')):
        #     return Category.objects.filter(is_delete=False, parent=None)
        # return Category.objects.filter(is_delete=False)
        # 只需要一级菜单列表，子集会在父级下
        return Category.objects.filter(is_delete=False, parent=None)


class ArticleViewset(CustomViewSet):
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [AllowAny],
                                    'update': [IsAuthenticated],
                                    'retrieve': [AllowAny],
                                    'destroy': [IsAuthenticated]
                                    }
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DrfPaginate
    search_fields = ['title', 'sub_title', 'content']
    filterset_fields = ['category']
    ordering_fields = ['sort', 'update_time', 'create_time']

    # 根据action获取权限
    def get_permissions(self):
        try:
            return [permissions() for permissions in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permissions() for permissions in self.permission_classes]

    # 获取菜单
    def get_queryset(self):
        return Article.objects.filter(is_delete=False)
