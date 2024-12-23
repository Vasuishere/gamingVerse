"""
WSGI config for webapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from webapp.wsgi import application  # Adjust "myproject" to your project name


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')

application = get_wsgi_application()



app = application

