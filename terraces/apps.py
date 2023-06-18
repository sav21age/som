from django.apps import AppConfig


class BridgesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'terraces'
    verbose_name = 'Терраса'

    def ready(self):
        import common.signals
