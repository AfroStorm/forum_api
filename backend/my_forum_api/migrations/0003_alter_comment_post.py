# Generated by Django 4.2.6 on 2023-10-06 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_forum_api', '0002_remove_userprofile_tags_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='my_forum_api.post'),
        ),
    ]
