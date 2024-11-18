from rest_framework import serializers
from .models import Post
from user_profile.serializers import ProfileSerializer


class PostSerializer(serializers.ModelSerializer):

    created_by = ProfileSerializer(source='created_by.profile', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at_formatted')
