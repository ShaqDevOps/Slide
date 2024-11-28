from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserCreateSerializer(BaseUserCreateSerializer):
    id = serializers.CharField(read_only=True)

    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'name', 'username', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email',)
