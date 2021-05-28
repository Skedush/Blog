from rest_framework import serializers
from .models import User, UserInfo


class UserSerializer(serializers.ModelSerializer):
    is_delete = serializers.HiddenField(default=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'is_superuser',
                  'gender',  'email', 'last_login',   'date_joined', 'is_delete')

    # 重写__init__方法，根据传入的fields字段序列化user
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(UserSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserInfoSerializer(serializers.ModelSerializer):
    # 获得user指定的属性
    user = UserSerializer(
        fields=('id', 'username', 'email', 'last_login', 'gender'))

    class Meta:
        model = UserInfo
        fields = ('id', 'phone', 'home', 'git', 'motton', 'user')
