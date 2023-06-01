from django.apps import AppConfig


class BlocksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blocks'
    verbose_name = 'Блоки'

    def ready(self):
        import common.signals