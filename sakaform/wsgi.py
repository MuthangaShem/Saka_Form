"""
WSGI config for sakaform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD
=======
from whitenoise.django import DjangoWhiteNoise
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sakaform.settings")

application = get_wsgi_application()
<<<<<<< HEAD
=======
application = DjangoWhiteNoise(application)
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
