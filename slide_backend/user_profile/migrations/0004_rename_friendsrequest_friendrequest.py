# Generated by Django 5.1.3 on 2024-11-20 01:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_profile_friends_friendsrequest'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FriendsRequest',
            new_name='FriendRequest',
        ),
    ]