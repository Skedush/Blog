from Blog.utils.customViewSet import CustomTokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Blog.apps.user.serializers import UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # 构建token方法
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data
        return data


class MyTokenObtainPairView(CustomTokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
