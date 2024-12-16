from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from .models import Post, Like, Comments
from .serializers import PostSerializer
from core.serializers import UserSerializer
from .forms import PostForm
from core.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


class PostViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # Get the 'user' query parameter
        user_param = self.request.query_params.get('user', None)

        if user_param == 'me':
            # Posts created by the logged-in user
            return Post.objects.filter(
                created_by=self.request.user
            ).select_related('created_by', 'created_by__profile')

        elif user_param == 'friends':
            # Get posts by friends of the logged-in user
            user_profile = self.request.user.profile  # Get the logged-in user's profile
            friends = user_profile.friends.values_list(
                'user__id', flat=True)  # Get the IDs of friends
            return Post.objects.filter(
                created_by__id__in=friends
            ).select_related('created_by', 'created_by__profile')

        elif user_param:
            # Posts created by a specific user (by ID)
            return Post.objects.filter(
                created_by__id=user_param
            ).select_related('created_by', 'created_by__profile')

        # Default: Return all posts
        return Post.objects.all().select_related('created_by', 'created_by__profile')

    serializer_class = PostSerializer
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


@api_view(['POST'])
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(created_by=request.user)

    if like in post.like.all():
        post.like.remove(like)
        post.likes_count -= 1
        liked = False
    else:
        post.like.add(like)
        post.likes_count += 1
        liked = True

    post.save()

    return Response({
        'likes_count': post.likes_count,
        'liked': liked
    }, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def post_comment(request, pk):
    # Get the post or return a 404 if not found
    post = get_object_or_404(Post, pk=pk)

    # Validate that the body is provided in the request
    body = request.data.get('body')
    if not body:
        return Response({'detail': 'Body of the comment is required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new comment associated with the authenticated user
    comment = Comments.objects.create(
        created_by=request.user,
        body=body
    )

    # Associate the comment with the post
    post.comments.add(comment)
    post.comments_count += 1
    post.save()

    # Return the updated comments_count and the newly created comment details
    return Response({
        'comments_count': post.comments_count,
        'comment': {
            'id': comment.id,
            'body': comment.body,
            'created_at': comment.created_at,  # Direct timestamp field
            'created_by': UserSerializer(comment.created_by).data
        }
    }, status=status.HTTP_201_CREATED)
