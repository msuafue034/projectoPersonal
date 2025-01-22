# settings/__init__.py
import os

ENV = os.getenv('DJANGO_ENV', 'production')  #? <-- Cambiar esta variable en producción por 'production'

if ENV == 'production':
    from .production import *
else:
    from .local import *