# profile/serializers.py
from rest_framework import serializers
from .models import FriendRequest, Profile
from django.contrib.auth import get_user_model
from core.serializers import UserSerializer


User = get_user_model()


class SimpleProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    name = serializers.CharField(source='user.name', read_only=True)
    id = serializers.CharField(source='user.id', read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'username', 'name', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    name = serializers.CharField(source='user.name', read_only=True)
    id = serializers.CharField(source='user.id', read_only=True)
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    friends = SimpleProfileSerializer(many=True, read_only=True)
    blocked_users = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)
    user = UserSerializer(read_only=True)
    friends_count = serializers.SerializerMethodField()
     

    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'name',
            'bio',
            'user',
            'profile_picture',
            'email',
            'state',
            'friends',
            'friends_count',
            'website',
            'followers',
            'created_at',
            'is_private',          # Privacy setting: public vs. private
            'is_active',           # Activity status: whether the user is online
            'last_seen',           # Timestamp of last activity
            'blocked_users'        # List of users this user has blocked
        ]
        read_only_fields = ['user', 'created_at', 'is_active', 'friends','friends_count',
                            'last_seen', 'followers', 'blocked_users']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = str(
            instance.user.id)  # Ensure id is a string
        return representation
    
    def get_friends_count(self, obj):
        # Calculate the friends count dynamically
        return obj.friends.count()

class FriendRequestSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    class Meta:
        model = FriendRequest
        fields = [
            'id',
            'sender',
            'receiver',
            'status',
            'sent_at',
        ]
        read_only_fields = ['id', 'sent_at', 'status']

    def get_sender(self, obj):
        # Access sender's profile explicitly
        sender_profile = obj.sender.profile
        return {
            "username": obj.sender.username,
            "name": obj.sender.name,
            "email": obj.sender.email,
            "friends_count": sender_profile.friends.count(),
            "bio": sender_profile.bio,
            "profile_picture": sender_profile.profile_picture.url if sender_profile.profile_picture else None,
            "is_active": sender_profile.is_active,
            "last_seen": sender_profile.last_seen,
        }

    def get_receiver(self, obj):
        # Access receiver's profile explicitly
        receiver_profile = obj.receiver.profile
        return {
            "username": obj.receiver.username,
            "name": obj.receiver.name,
            "email": obj.receiver.email,
            "friends_count": receiver_profile.friends.count(),
            "bio": receiver_profile.bio,
            "profile_picture": receiver_profile.profile_picture.url if receiver_profile.profile_picture else None,
            "is_active": receiver_profile.is_active,
            "last_seen": receiver_profile.last_seen,
        }
