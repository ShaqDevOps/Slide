from django.db import models
from django.conf import settings
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="following", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # False = Public, True = Private
    is_private = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    last_seen = models.DateTimeField(null=True, blank=True)

    blocked_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="blocked_by", blank=True)

    # Method to update last_seen timestamp

    def update_last_seen(self):
        self.last_seen = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.user.username}'s Profile"
