from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    """
    A tag that can be attached to a post to highlight it 
    """
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.caption


class UserProfile(models.Model):
    """
    A profile for every user
    """
    profile_image = models.CharField(
        max_length=500,
        default='https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait'
                '_Placeholder.png'
    )
    about_me = models.TextField(
        max_length=500,
        blank=True
    )
    last_login = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)

    owner = models.OneToOneField(
        User,
        related_name='userprofile',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'Profile: {self.owner.username}'


class Post(models.Model):
    """
    A post that can be created by a user in the forum app
    """
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    user_profile = models.ForeignKey(
        UserProfile,
        related_name='posts',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """
    A comment that can be placed under a post of a user
    """
    content = models.TextField(max_length=289)
    created_on = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
    user_profile = models.ForeignKey(
        UserProfile,
        related_name='comments',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.created_on} - {self.content}'
