import os
from som.settings import BASE_DIR

def str2bool(s):
    if s in ('1', 'True'):
        return True
    elif s in ('0', 'False'):
        return False
    else:
        raise ValueError("Cannot covert {} to a bool".format(s))

DEBUG = str2bool(os.environ.get("DEBUG"))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
SECRET_KEY = os.environ.get("SECRET_KEY")

ADMINS = ((os.environ.get('EMAIL'),), )
LIST_OF_EMAIL_RECIPIENTS = (os.environ.get('EMAIL'), )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'ATOMIC_REQUESTS': True,
    }
}

EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL")
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")  # str comming, maybe need num
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = SERVER_EMAIL = EMAIL_HOST_USER

RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')

COMPRESS_ENABLED = True

# CACHE_BACKEND = "django.core.cache.backends.dummy.DummyCache"
CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'

CACHE_TIMEOUT = os.environ.get("CACHE_TIMEOUT")
CACHES = {
    'default': {
        'BACKEND': CACHE_BACKEND,
        'TIMEOUT': CACHE_TIMEOUT,
    },
    'axes': {
        'BACKEND': CACHE_BACKEND,
    },
    'file_resubmit': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(os.path.join(BASE_DIR, 'cache'), 'file_resubmit'),
    },
}