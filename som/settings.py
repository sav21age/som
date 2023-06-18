import os
from pathlib import Path

import locale
def getpreferredencoding(do_setlocale = True):
    return "utf-8"
locale.getpreferredencoding = getpreferredencoding

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'markdownify.apps.MarkdownifyConfig',
    # 'sekizai',
    'django_db_logger',
    'compressor',
    'easy_thumbnails',
    'solo',
    'reset_migrations',
    'blocks',
    'index',
    'calculator',
    'images',
    'videos',
    'staircases',
    'railings',
    'porch',
    # 'steps',
    'terraces',
    'bridges',
    'contacts',
    'callback',
    'common',
    'file_resubmit',
    "crispy_forms",
    "crispy_bootstrap5",
    'axes',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'som.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'sekizai.context_processors.sekizai',
                'common.context_processors.main',
            ],
        },
    },
]

WSGI_APPLICATION = 'som.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

# COMPRESS_ROOT = STATIC_ROOT

COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.SlimItFilter',]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MARKDOWNIFY = {
    "default": {
        "WHITELIST_TAGS": [
            'a',
            'abbr',
            'acronym',
            'b',
            'blockquote',
            'em',
            'i',
            'li',
            'ol',
            'p',
            'strong',
            'ul',
            'h1',
            'h2',
            'h3',
            'h4',
            'h5',
            'h6',
        ]
    }
}

THUMBNAIL_BASEDIR = 'i'
# THUMBNAIL_SUBDIR = 'thumbs'
# THUMBNAIL_QUALITY = 95
THUMBNAIL_DEBUG = False
THUMBNAIL_PRESERVE_EXTENSIONS = ('png', 'gif')
# THUMBNAIL_NAMER = 'easy_thumbnails.namers.hashed'
THUMBNAIL_HIGHRES_INFIX = '@2x'

THUMBNAIL_ALIASES = {
    '': {
        '360w_poor': {'crop': 'smart', 'size': (360, 360), 'quality': 10, 'bw': True},
        '360w': {'crop': 'smart', 'size': (360, 360), 'quality': 95, },

        '720w_poor': {'crop': 'smart', 'size': (720, 720), 'quality': 10, 'bw': True},
        '720w': {'crop': 'smart', 'size': (720, 720), 'quality': 95, },

        '1080w_poor': {'crop': 'smart', 'size': (1080, 1080), 'quality': 10, 'bw': True},
        '1080w': {'crop': 'smart', 'size': (1080, 1080), 'quality': 95, },

        '1920w_poor': {'crop': 'scale', 'size': (1920, 1920), 'quality': 10, 'bw': True},
        '1920w': {'crop': 'scale', 'size': (1920, 1920), 'quality': 95, },
    }
    # '': {
    #     '360w_poor': {'crop': 'scale', 'size': (360, 360), 'quality': 10, 'bw': True},
    #     '360w': {'crop': 'scale', 'size': (360, 360), 'quality': 95, },

    #     '720w_poor': {'crop': 'scale', 'size': (720, 720), 'quality': 10, 'bw': True},
    #     '720w': {'crop': 'scale', 'size': (720, 720), 'quality': 95, },

    #     '1080w_poor': {'crop': 'scale', 'size': (1080, 1080), 'quality': 10, 'bw': True},
    #     '1080w': {'crop': 'scale', 'size': (1080, 1080), 'quality': 95, },

    #     '1920w_poor': {'crop': 'scale', 'size': (1920, 1920), 'quality': 10, 'bw': True},
    #     '1920w': {'crop': 'scale', 'size': (1920, 1920), 'quality': 95, },
    # }
}

# RECAPTCHA_DEFAULT_ACTION = 'generic'
# RECAPTCHA_SCORE_THRESHOLD = 0.5
# RECAPTCHA_LANGUAGE = 'ru'

DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE = 50
DJANGO_DB_LOGGER_ENABLE_FORMATTER = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'db_log': {
            'level': 'DEBUG',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler'
        },
    },
    'loggers': {
        'db': {
            'handlers': ['db_log'],
            'level': 'DEBUG'
        },
        'django.request': {  # logging 500 errors to database
            'handlers': ['db_log'],
            'level': 'INFO',
            # 'level': 'ERROR',
            'propagate': False,
        }
    }
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
# CRISPY_CLASS_CONVERTERS = {'numberinput': "form-range",}

if os.environ.get("DEBUG"):
    try:
        from som.settings_docker import *
    except ImportError:
        raise ImportError("Couldn't import settings_docker.py")
else:
    try:
        from som.settings_local import *
    except ImportError:
        raise ImportError("Couldn't import settings_local.py")
