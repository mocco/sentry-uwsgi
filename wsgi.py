#!/usr/bin/env python
import os, sys

from django.conf import settings

if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

os.environ['CELERY_LOADER'] = 'django'

from django.core.wsgi import get_wsgi_application
from raven.contrib.django.middleware.wsgi import Sentry

application = Sentry(get_wsgi_application())