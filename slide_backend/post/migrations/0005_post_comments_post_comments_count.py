# Generated by Django 5.1.3 on 2024-12-15 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='post_comments', to='post.comments'),
        ),
        migrations.AddField(
            model_name='post',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
    ]
