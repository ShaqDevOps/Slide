import uuid
from django.db import models
from django.conf import settings
from django.utils.timesince import timesince


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='post_attachments', on_delete=models.CASCADE)


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='post_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=350, blank=True, null=True)

    def created_at_formatted(self):
        return timesince(self.created_at)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(max_length=350, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    attachments = models.ManyToManyField(PostAttachment, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def created_at_formatted(self):
        return timesince(self.created_at)

    like = models.ManyToManyField(Like, blank=True, related_name='post_likes')
    likes_count = models.IntegerField(default=0)

    comments = models.ManyToManyField(
        Comments, blank=True, related_name='post_comments')

    comments_count = models.IntegerField(default=0)
