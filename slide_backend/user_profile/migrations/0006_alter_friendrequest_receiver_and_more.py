# Generated by Django 5.1.3 on 2024-12-03 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_rename_sent_to_friendrequest_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_friend_requests', to='user_profile.profile'),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_friend_requests', to='user_profile.profile'),
        ),
    ]