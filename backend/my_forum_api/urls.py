from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileView, TagView, CommentView, PostView, UserView

router = DefaultRouter()
router.register(r'users', UserView)
router.register(r'user-profiles', UserProfileView)
router.register(r'tags', TagView)
router.register(r'comments', CommentView)
router.register(r'posts', PostView)


urlpatterns = [
    path('', include(router.urls))
]
