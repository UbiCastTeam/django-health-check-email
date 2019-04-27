from django.apps import AppConfig
from django.conf import settings
from health_check.plugins import plugin_dir


class HealthCheckEmailConfig(AppConfig):
    name = "health_check_email"

    def ready(self):
        if (
            hasattr(settings, "HEALTH_CHECK")
            and ("EMAIL_ENABLED" in settings.HEALTH_CHECK)
            and not settings.HEALTH_CHECK["EMAIL_ENABLED"]
        ):
            pass
        else:
            from .backends import EmailBackend

            plugin_dir.register(EmailBackend)
