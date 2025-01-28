# settings/__init__.py
import os

ENV = os.getenv('DJANGO_ENV', 'local')  #? <-- Cambiar esta variable entre 'local' y 'production'

if ENV == 'production':
    from .production import *
else:
    from .local import *