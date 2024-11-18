# profile/serializers.py
from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    name = serializers.CharField(source='user.name', read_only=True)
    id = serializers.CharField(source='user.id', read_only=True)
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    blocked_users = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'name',
            'bio',
            'profile_picture',
            'email',
            'state',
            'website',
            'followers',
            'created_at',
            'is_private',          # Privacy setting: public vs. private
            'is_active',           # Activity status: whether the user is online
            'last_seen',           # Timestamp of last activity
            'blocked_users'        # List of users this user has blocked
        ]
        read_only_fields = ['user', 'created_at', 'is_active',
                            'last_seen', 'followers', 'blocked_users']

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['id'] = str(
                instance.user.id)  # Ensure id is a string
            return representation
