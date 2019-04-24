# django-health-check-email

This is a plugin for [django-health-check](https://github.com/KristianOellegaard/django-health-check), which check that your app can send emails through the email backend configured in your Django settings.

## Installation

Install with pip in your environment:

```bash
pip install django-health-check django-health-check-email
```

Add the app to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'health_check',                             # required
    # ...
    'health_check_email',
]
```

Apply migrations:

```bash
python manage.py migrate
```

## Configuration

Add your settings to `HEALTH_CHECK`:

```python
HEALTH_CHECK = {
    "EMAIL_ENABLED": True,
    "EMAIL_IS_CRITICAL": True,
    "EMAIL_SUBJECT": "my email health check",
    "EMAIL_MESSAGE": "my message",
    "EMAIL_FROM": "test@example.com",
    "EMAIL_TO": ["admin@example.com", "dev@example.com"],
}
```
