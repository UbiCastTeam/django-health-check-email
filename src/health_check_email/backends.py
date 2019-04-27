from smtplib import SMTPException

from django.core.mail import send_mail
from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import HealthCheckException

from .conf import HEALTH_CHECK

EMAIL_IS_CRITICAL = HEALTH_CHECK["EMAIL_IS_CRITICAL"]
EMAIL_SUBJECT = HEALTH_CHECK["EMAIL_SUBJECT"]
EMAIL_MESSAGE = HEALTH_CHECK["EMAIL_MESSAGE"]
EMAIL_FROM = HEALTH_CHECK["EMAIL_FROM"]
EMAIL_TO = HEALTH_CHECK["EMAIL_TO"]


class EmailBackend(BaseHealthCheckBackend):
    critical_service = True

    def check_status(self):
        try:
            send_mail(EMAIL_SUBJECT, EMAIL_MESSAGE, EMAIL_FROM, EMAIL_TO)
        except SMTPException as message:
            raise HealthCheckException(message)

    def identifier(self):
        return self.__class__.__name__
