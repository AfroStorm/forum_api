from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


user = get_user_model()


class CustomModelBackend(ModelBackend):
    """
    A custom model backend to override the django default model backend
    """

    def login_date_create_date_sync(self, user):
        """
        Update the last_login field of the userprofile model through the
        last_login field of the django user model
        """
        user.userprofile.last_login = user.last_login
        user.userprofile.created_on = user.date_joined
        user.userprofile.save()
