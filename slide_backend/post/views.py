from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from .models import Post
from .serializers import PostSerializer
from core.serializers import UserSerializer
from .forms import PostForm
from core.models import User
from django.http import JsonResponse


class PostViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # Check if the 'user' query parameter is set to 'me'
        user_param = self.request.query_params.get('user', None)
        if user_param == 'me':
            return Post.objects.filter(created_by=self.request.user).select_related('created_by', 'created_by__profile')
        # Otherwise, return all posts
        return Post.objects.all().select_related('created_by', 'created_by__profile')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    # To handle both JSON and form data
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def create(self, request, *args, **kwargs):
        if request.content_type == 'application/json':
            # Handle JSON data
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            # Handle form data
            form = PostForm(request.data, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.created_by = request.user
                # Additional validation logic
                if not self.custom_validation(post):
                    return Response({'detail': 'Custom validation failed.'}, status=status.HTTP_400_BAD_REQUEST)
                post.save()
                serializer = self.get_serializer(post)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    def custom_validation(self, post):
        # Implement your custom validation logic here
        # Return True if validation passes, False otherwise
        return True

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
