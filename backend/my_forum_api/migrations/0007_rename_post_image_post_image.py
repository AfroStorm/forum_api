# Generated by Django 4.2.6 on 2023-10-09 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_forum_api', '0006_post_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_image',
            new_name='image',
        ),
    ]
