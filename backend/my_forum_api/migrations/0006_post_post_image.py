# Generated by Django 4.2.6 on 2023-10-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_forum_api', '0005_rename_owner_comment_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.CharField(default='https://t3.ftcdn.net/jpg/02/48/42/64/360_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg', max_length=500),
        ),
    ]
