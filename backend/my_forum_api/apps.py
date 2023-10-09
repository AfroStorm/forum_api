from django.apps import AppConfig


class MyForumApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_forum_api'

    def ready(self) -> None:
        import my_forum_api.api.signals
        return super().ready()
