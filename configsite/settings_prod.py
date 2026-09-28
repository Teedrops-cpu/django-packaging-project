import os

from .settings import *  # noqa: F401,F403

DEBUG = False

# Secrets come from the environment; missing values fail loudly at startup.
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = os.environ["DJANGO_ALLOWED_HOSTS"].split(",")

# HTTPS hardening (these clear W004, W008, W012, W016)
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600  # start small; raise it only once HTTPS is confirmed working
