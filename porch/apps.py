from django.apps import AppConfig


class PorchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'porch'
    verbose_name = 'Крыльцо'

    def ready(self):
        import common.signals
