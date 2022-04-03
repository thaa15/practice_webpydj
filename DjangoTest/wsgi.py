"""Web Server Gateway Interface"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoTest.settings')

application = get_wsgi_application()
