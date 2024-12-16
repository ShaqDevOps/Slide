from django.urls import path
from . import views

urlpatterns = [

    path('profiles/<uuid:id>/',
         views.ProfileDetailView.as_view(), name='profile-detail'),
    path('me/', views.MeView.as_view(), name='me'),
    path('profiles/<uuid:pk>/friends/', views.friends, name='friends'),
    path('profiles/<uuid:pk>/friends/request/send/',
         views.send_friend_request, name='send-friend-request'),
    path('profiles/friends/request/response/',
         views.friend_request_response, name="friend-request-response"),
    path('logout/', views.logout_view, name='logout')


]
