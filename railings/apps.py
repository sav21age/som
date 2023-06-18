from django.apps import AppConfig


class RailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'railings'
    verbose_name = 'Ограждения'

    def ready(self):
        import common.signals
