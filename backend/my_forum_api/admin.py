from django.contrib import admin
from .models import UserProfile, Tag, Comment, Post
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Post)
