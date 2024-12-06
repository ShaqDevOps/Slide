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
    try:
        # Get the receiver's User instance
        receiver = User.objects.get(id=pk)

        # Get the sender's User instance (currently logged-in user)
        sender = request.user

        # Check if a FriendRequest already exists between sender and receiver
        existing_request = FriendRequest.objects.filter(
            sender=sender, receiver=receiver
        ).exists() or FriendRequest.objects.filter(
            sender=receiver, receiver=sender
        ).exists()

        if not existing_request:
            # Create the FriendRequest instance
            FriendRequest.objects.create(
                sender=sender,
                receiver=receiver,
                status=FriendRequest.SENT
            )
            return JsonResponse({'message': 'Friend Request Sent'}, status=201)
        else:
            # Use a 409 Conflict status code to indicate a logical conflict
            return JsonResponse({'message': 'Request already sent'})
    except User.DoesNotExist:
        # Return 404 if the receiver does not exist
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        # Catch all other exceptions and return a 500 status
        print(f"Unexpected error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['GET'])
def friends_list(request, id):
    try:
        # Get the user instance
        user = User.objects.get(id=id)

        # Retrieve the user's friends
        friends = user.profile.friends.all()

        # Serialize the friends
        friends_serializer = ProfileSerializer(friends, many=True)

        return JsonResponse({'friends': friends_serializer.data}, status=200)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['PATCH'])
def friend_request_response(request):
    try:
        # Fetch the FriendRequest using the provided ID
        friend_request = get_object_or_404(FriendRequest, id=request.data.get('id'))

        # Get the status from the request
        request_status = request.data.get('request_status')
        if request_status not in ['accept', 'ignore']:
            return Response({"error": "Invalid status"}, status=400)

        if request_status == 'accept':
            friend_request.status = FriendRequest.ACCEPTED

            # Access profiles of sender and receiver
            sender_profile = friend_request.sender.profile
            receiver_profile = friend_request.receiver.profile

            # Add each other to the friends list
            sender_profile.friends.add(receiver_profile)
            receiver_profile.friends.add(sender_profile)

        elif request_status == 'ignore':
            friend_request.status = FriendRequest.REJECTED

        # Save the updated FriendRequest
        friend_request.save()

        return Response({"message": f"Request {request_status}ed successfully"}, status=200)

    except FriendRequest.DoesNotExist:
        return Response({"error": "Friend request not found"}, status=404)
    except Exception as e:
        # Log unexpected error for debugging
        print(f"Unexpected error: {str(e)}")
        return Response({"error": str(e)}, status=500)



@api_view(['GET'])
def friends(request, pk):
    try:
        # Get the user instance

        user = User.objects.get(id=pk)

        # Get the user's profile

        profile = user.profile

        # Fetch friends through the profile
        friends = profile.friends.all()

        # Serialize friends
        friends_serializer = ProfileSerializer(friends, many=True)

        # Fetch friend requests if the logged-in user is viewing their own profile
        requests = []
        if user == request.user:
            friend_requests = FriendRequest.objects.filter(
                receiver=request.user, status=FriendRequest.SENT
            )
            requests_serializer = FriendRequestSerializer(friend_requests, many=True)
            requests = requests_serializer.data

        # Combine friends and requests
        return JsonResponse({
            'friends': friends_serializer.data,
            'requests': requests
        }, safe=False)

    except User.DoesNotExist:
        print("User not found")
        return JsonResponse({'error': 'User not found'}, status=404)

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)
