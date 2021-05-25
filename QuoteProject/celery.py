# Reference https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QuoteProject.settings")

# creating a celery app
app = Celery("QuoteProject")

# You can tell your Celery instance to use a configuration module by calling the app.config_from_object() method
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover task modules.
# Searches a list of packages for a “tasks.py” module.
app.autodiscover_tasks()