from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from .models import UserProfile, Tag, Comment, Post
from .permissions import IsReadOnly, IsOwnerOrReadOnly, IsListOnly
from .serializers import UserProfileSerializer, TagSerializer,\
    CommentSerializer, PostSerializer, UserSerialier
# Create your views here.


class UserView(ModelViewSet):
    """
    Handles browsable User API
    """

    queryset = User.objects.all()
    serializer_class = UserSerialier
    permission_classes = [IsOwnerOrReadOnly]


class UserProfileView(ModelViewSet):
    """
    Handles browsable UserProfile API
    """

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly, IsListOnly]


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
    permission_classes = [IsListOnly, IsOwnerOrReadOnly]


class PostView(ModelViewSet):
    """
    Handles browsable Post API
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
