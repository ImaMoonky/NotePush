from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

application = get_wsgi_application()