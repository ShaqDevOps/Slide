from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import Profile
from .serializers import FriendRequestSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models import User
from .models import FriendRequest
from rest_framework.decorators import api_view


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=200)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found"}, status=404)


class ProfileDetailView(generics.RetrieveAPIView):
    """
    View for retrieving any user's profile based on user ID.
    """

    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'user_id'  # the name in the model -> backend
    lookup_url_kwarg = 'id'  # the name in the front end

    def get_queryset(self):
        # Get the lookup parameter from the URL
        profile_id = self.kwargs.get(self.lookup_url_kwarg)

        # Return a filtered queryset
        return Profile.objects.filter(user__id=profile_id)


@api_view(['POST'])
def send_friend_request(request, pk):

    receiving_user_id = pk

    receiving_user = User.objects.get(id=receiving_user_id)
    sending_user = request.user

    FriendRequest.objects.create(
        receiver=receiving_user, sender=sending_user)

    return JsonResponse({'message': 'Friend Request Sent'})


api_view(['GET'])


def friends_list(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)

    friends = profile.friends

    friends = ProfileSerializer(friends, many=True)
    print(friends)

    return JsonResponse({'friends': friends.data})


@api_view(['PATCH'])
def friend_request_response(request):
    print('friend_request id received: ', request.data.get('id'))

    if request.method == 'PATCH':
        try:
            # Fetch status from the payload
            request_status = request.data.get('request_status')
            print('Request status received:', request_status)  # Debugging log
            if not request_status or request_status not in ['accept', 'ignore']:
                return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

            # Process the status (accept or ignore)
            # Grab 'id' that is passed in payload
            friend_request = get_object_or_404(
                FriendRequest, id=request.data.get('id'))

            # Update the status based on the request
            if request_status == 'accept':
                friend_request.status = FriendRequest.ACCEPTED

                # Add the users to eachother's friends lit
                friend_request.receiver.profile.friends.add(
                    friend_request.sender.profile)

                friend_request.sender.profile.friends.add(
                    friend_request.receiver.profile)

            elif request_status == 'ignore':
                friend_request.status = FriendRequest.REJECTED
            friend_request.save()

            # Log updated status
            print('Updated FriendRequest:', friend_request.status)

            return Response({"message": f"Request {request_status}ed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            print('Exception occurred:', str(e))  # Debugging log for exception
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def friends(request, pk):
    profile = Profile.objects.get(user_id=pk)
    signed_in_user = request.user
    user = profile.user
    requests = []

    # If the user is the signed-in user, get their friend requests
    if user == signed_in_user:
        friend_requests = FriendRequest.objects.filter(receiver=signed_in_user)
        requests_serializer = FriendRequestSerializer(
            friend_requests, many=True)
        requests = requests_serializer.data  # Convert to list of serialized data

    # Get friends and serialize
    friends = profile.friends.all()
    friends_serializer = ProfileSerializer(friends, many=True)

    # Debugging print statement
    print(f'{friends_serializer.data} + {requests}')

    # Combine friends and requests in a single dictionary
    return JsonResponse({
        'friends': friends_serializer.data,  # List of serialized friends
        'requests': requests  # List of serialized friend requests
    }, safe=False)
