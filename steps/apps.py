from django.apps import AppConfig


class StepsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'steps'
    verbose_name = 'Ступени'

    def ready(self):
        import common.signals