from .base import *

DEBUG = False

ALLOWED_HOSTS = ['obeidarash.ir', 'www.obeidarash.ir']

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
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
