from rest_framework import serializers
from .models import Post, Comments
from user_profile.serializers import ProfileSerializer


class CommentSerializer(serializers.ModelSerializer):
    created_by = ProfileSerializer(source='created_by.profile', read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'body', 'created_by', 'created_at_formatted')


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    created_by = ProfileSerializer(source='created_by.profile', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'body', 'likes_count', 'comments', 'comments_count',
                  'created_by', 'created_at_formatted')
