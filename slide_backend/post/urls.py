# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# Create a router and register the PostViewSet
router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
]
