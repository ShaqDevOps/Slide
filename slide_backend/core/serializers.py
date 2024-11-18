from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from user_profile.serializers import ProfileSerializer


User = get_user_model()


class CustomUserCreateSerializer(BaseUserCreateSerializer):
    id = serializers.CharField(read_only=True)

    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'name', 'username', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)
    id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'profile')
