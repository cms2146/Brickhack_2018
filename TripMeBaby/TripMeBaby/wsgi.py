"""
WSGI config for TripMeBaby project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opt.bitnami.apps.django.django_projects.Brickhack_2018.TripMeBaby.TripMeBaby.settings")

application = get_wsgi_application()
