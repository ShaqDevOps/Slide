from django.urls import path
from .views import ProfileDetailView, MeView

urlpatterns = [

    path('profiles/<user_id>/',
         ProfileDetailView.as_view(), name='profile-detail'),
    path('me/', MeView.as_view(), name='me')
]
