from django.apps import AppConfig


class AlertConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alert'

    # define notificator background
    def ready(self):
        from notificator import updater
        updater.start()
