from django.apps import AppConfig


class AppConfig(AppConfig):  # noqa
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
