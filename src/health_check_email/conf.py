from health_check.conf import HEALTH_CHECK

HEALTH_CHECK.setdefault("EMAIL_ENABLED", False)
HEALTH_CHECK.setdefault("EMAIL_IS_CRITICAL", True)
HEALTH_CHECK.setdefault("EMAIL_SUBJECT", "email health check")
HEALTH_CHECK.setdefault("EMAIL_MESSAGE", "")
HEALTH_CHECK.setdefault("EMAIL_FROM", "healthcheck+email@localhost")
HEALTH_CHECK.setdefault("EMAIL_TO", ["root@localhost"])
