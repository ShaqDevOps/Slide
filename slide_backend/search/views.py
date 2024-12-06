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
    query = data.get('query', '')

    print('query', query)

    # Filter users by username containing the query
    users = User.objects.filter(username__icontains=query)

    # Serialize users and include friends_count
    user_data = []
    for user in users:
        profile = getattr(user, 'profile', None)  # Get the profile for the user
        user_data.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'friends_count': profile.friends.count() if profile else 0,  # Safely get friends_count
        })

    # Filter posts by body containing the query
    posts = Post.objects.filter(body__icontains=query)
    post_list = PostSerializer(posts, many=True)

    return JsonResponse({'users': user_data, 'posts': post_list.data}, safe=False)