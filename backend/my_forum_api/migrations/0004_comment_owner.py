# Generated by Django 4.2.6 on 2023-10-07 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_forum_api', '0003_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='my_forum_api.userprofile'),
        ),
    ]
