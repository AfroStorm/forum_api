from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserView)
router.register(r'user-profiles', views.UserProfileView)
router.register(r'tags', views.TagView)
router.register(r'comments', views.CommentView)
router.register(r'posts', views.PostView)


urlpatterns = [
    path('posts/<int:pk>/create/comment/',
         views.CreateCommentView.as_view(), name='create_comment_url'),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
