from .base import *


DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# DATABASES = {
#     'default': {
#         'ENGINE': 'mysql.connector.django',  # O 'django.db.backends.mysql' si usas mysqlclient
#         'NAME': config('2DAW_MNSF_BD'),
#         'USER': config('msuafue034'),
#         'PASSWORD': config('msuafue034!'),
#         'HOST': config('192.168.100.5', default='localhost'),
#         'PORT': config('3306', default='3306'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',     # Motor para mysql-connector-python
        'NAME': '2DAW_MNSF_BD',                 # Nombre de la base de datos
        'USER': 'msuafue034',                   # Usuario de la base de datos
        'PASSWORD': 'msuafue034!',              # Contraseña del usuario
        'HOST': '192.168.100.5',                # Dirección del servidor
        'PORT': '3306',                         # Puerto de la base de datos
        'OPTIONS': {
            'autocommit': True,
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# # Configuración del backend de correo para producción
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')