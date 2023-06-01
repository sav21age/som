from django.apps import AppConfig


class IndexConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index'
    verbose_name = 'Главная страница'
    
    def ready(self):
        import common.signals