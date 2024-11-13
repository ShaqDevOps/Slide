from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    created_by = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at')
