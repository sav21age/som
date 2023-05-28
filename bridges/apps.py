from django.apps import AppConfig


class BridgesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bridges'
    verbose_name = 'Мостик'

    def ready(self):
        import common.signals
