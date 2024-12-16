# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register the PostViewSet
router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='post')

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),
    path('posts/<uuid:pk>/like/', views.post_like),
    path('posts/<uuid:pk>/comment/', views.post_comment, name='post-comment'),

]
