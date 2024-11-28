from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from post.serializers import PostSerializer
from user_profile.models import Profile
from core.models import User
from post.models import Post
from core.serializers import UserSerializer


@api_view(['POST'])
def search(request):
    data = request.data
    query = data['query']

    print('query', query)

    # Filter users by username or email containing the query
    users = User.objects.filter(
        username__icontains=query)
    user_list = UserSerializer(users, many=True)

    posts = Post.objects.filter(body__icontains=query)

    post_list = PostSerializer(posts, many=True)

    return JsonResponse({'users': user_list.data, 'posts': post_list.data}, safe=False)
