from typing import Any
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from .models import UserProfile, Tag, Comment, Post
from .permissions import IsReadOnly, IoroPost,\
    IoroUser, IsListOnly, IoroUserProfile,\
    IoroComment
from .serializers import UserProfileSerializer, TagSerializer,\
    CommentSerializer, PostSerializer, UserSerialier
# Create your views here.


class UserView(ModelViewSet):
    """
    Handles browsable User API
    """

    queryset = User.objects.all()
    serializer_class = UserSerialier
    permission_classes = [IoroUser]


class UserProfileView(ModelViewSet):
    """
    Handles browsable UserProfile API
    """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsListOnly, IoroUserProfile]


class TagView(ModelViewSet):
    """
    Handles browsable Tag API
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsReadOnly, IsListOnly]


class CommentView(ModelViewSet):
    """
    Handles browsable Comment API
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsListOnly, IoroComment]


class PostView(ModelViewSet):
    """
    Handles browsable Post API
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticatedOrReadOnly, IoroPost]

    def perform_create(self, serializer):
        """
        Sets the value of the user_profile field to the authenticated users
        userprofile
        """
        serializer.save(user_profile=self.request.user.userprofile)


class CreateCommentView(generics.CreateAPIView):
    """
    Creates a comment and links it to a post
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        post = self.kwargs['pk']
        try:
            post = Post.objects.get(pk=post)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found!'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer.save(post=post, user_profile=self.request.user.userprofile)


class UserLoginApiView(ObtainAuthToken):
    """
    Handles creating user authentication tokens
    """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
