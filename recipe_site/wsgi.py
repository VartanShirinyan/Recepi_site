"""
WSGI config for recipe_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
path = '/home/VartanS/Recepi_site-Django'
if path not in sys.path:
    sys.path.append(path)
    
os.environ['DJANGO_SETTINGS_MODULE'] = 'recipe_site.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
