# profile/serializers.py
from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    blocked_users = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user',
            'bio',
            'profile_picture',
            'location',
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
