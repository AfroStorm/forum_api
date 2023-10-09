from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from my_forum_api.models import Post, Comment, Tag, UserProfile
from django.contrib.auth.models import User


class IndexView(ListView):
    """
    Lists the 3 most recent posts
    """

    template_name = 'my_forum_api/index.html'
    queryset = Post.objects.all().order_by('-created_on')[:3]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        query_set = self.queryset
        context['first_post'] = query_set[0]
        context['second_post'] = query_set[1]
        context['third_post'] = query_set[2]
        return context
