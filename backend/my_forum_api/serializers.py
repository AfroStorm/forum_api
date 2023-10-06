from rest_framework import serializers
from .models import UserProfile, Tag, Comment, Post
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    """
    Serializes the UserProfile
    """
    posts = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Post.objects.all()
    )

    class Meta:
        model = UserProfile
        fields = ['id', 'profile_image', 'about_me',
                  'last_login', 'created_on', 'owner',
                  'posts']
        extra_kwargs = {
            'owner': {'read_only': True},
        }


class UserSerialier(serializers.ModelSerializer):
    """
    Serialzes the in-built User class of django
    """
    userprofile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'userprofile']


class TagSerializer(serializers.ModelSerializer):
    """
    Serializes the Tag
    """
    class Meta:
        model = Tag
        fields = ['id', 'caption']
        extra_kwargs = {
            'caption': {'read_only': True}
        }


class PostSerializer(serializers.ModelSerializer):
    """
    Serializes the Post
    """
    comments = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='caption'
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_on',
                  'edited', 'user_profile', 'tags', 'comments']
        extra_kwargs = {
            'user_profile': {'read_only': True},
        }


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes the comment
    """
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_on', 'edited', 'post']
        extra_kwargs = {
            'post': {'read_only': True},
        }
