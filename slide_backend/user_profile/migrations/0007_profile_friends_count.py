# Generated by Django 5.1.3 on 2024-12-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_alter_friendrequest_receiver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends_count',
            field=models.IntegerField(default=0),
        ),
    ]
