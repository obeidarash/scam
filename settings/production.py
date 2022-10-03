from .base import *

DEBUG = False

ALLOWED_HOSTS = ['isitnowruz.ir', 'www.isitnowruz.ir']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'obeidara_thisisatest',  # database name
        'USER': 'obeidara_testuser',
        'PASSWORD': 'auLE&mu~Zd.W',
        'HOST': 'obeidarash.ir',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
