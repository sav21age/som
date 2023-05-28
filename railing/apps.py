from django.apps import AppConfig


class RailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'railing'
    verbose_name = 'Перила'

    def ready(self):
        import common.signals
