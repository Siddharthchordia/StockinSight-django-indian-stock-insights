from django.apps import AppConfig
from django.db.models.signals import post_migrate

class StocksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "stocks"

    def ready(self):
        from .signals import create_metric_categories
        post_migrate.connect(create_metric_categories, sender=self)
