from django.urls import path, include
from my_forum_api import views


urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index_url')
]
