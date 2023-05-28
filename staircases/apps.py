from django.apps import AppConfig


class StaircasesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staircases'
    verbose_name = 'Лестницы'

    def ready(self):
        import common.signals
