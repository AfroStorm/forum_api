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
    permission_classes = [IsAuthenticatedOrReadOnly, IoroPost]

    def perform_create(self, serializer):
        """
        Sets the value of the user_profile field to the authenticated users
        userprofile
        """
        serializer.save(user_profile=self.request.user.userprofile)
