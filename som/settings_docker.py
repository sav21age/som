import os

DEBUG = os.environ.get("DEBUG")
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