from .base import *

DEBUG = False

ALLOWED_HOSTS = ['shortinvestincoin.com', 'www.shortinvestincoin.com']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'isitnowr_thenewprojectdata',  # database name
        'USER': 'isitnowr_thisissuperuserusername',
        'PASSWORD': 'auLE&mu~Zd.W',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
