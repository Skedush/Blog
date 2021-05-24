from rest_framework import serializers
from .models import Category, Article


class CategorySerializer(serializers.ModelSerializer):
    is_delete = serializers.HiddenField(default=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'create_time',
                  'update_time', 'parent', 'is_delete', 'describe')


class MenuSerializer(serializers.ModelSerializer):
    is_delete = serializers.HiddenField(default=False)
    children = serializers.SerializerMethodField("get_children")

    def get_children(self, obj):
        # 自关联字段
        serializer = MenuSerializer(
            instance=obj.children.all(),
            many=True,
            read_only=True,
        )
        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'name', 'create_time',
                  'update_time', 'is_delete', 'children', 'describe')


class ArticleSerializer(serializers.ModelSerializer):
    is_delete = serializers.HiddenField(default=False)

    class Meta:
        model = Article
        fields = ('id', 'title', 'create_time',
                  'update_time', 'is_delete', 'sub_title', 'content', 'category')
