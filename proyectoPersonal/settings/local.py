from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'noeliasf.ieshm.org']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

