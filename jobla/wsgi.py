"""
WSGI config for jobla project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobla.settings")

application = get_wsgi_application()

#Utiliser whitenoise pour héberger les fichiers dans Heroku
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
