from .base import *
from dotenv import load_dotenv
import os


DEBUG = False
ADMINS = (
    ('konradfolwarski', 'konrad.folwarski.dev@gmail.com'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
