import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'markdownify.apps.MarkdownifyConfig',
    'snowpenguin.django.recaptcha3',
    # 'sekizai',
    'django_db_logger',
    'compressor',
    'mdeditor',
    'martor',
    'easy_thumbnails',
    'solo',
    'reset_migrations',
    'debug_toolbar',
    'blocks',
    'index',
    'images',
    'staircases',
    'railing',
    'porch',
    'steps',
    'bridges',
    'contacts',
    'callback',
    'common',
    'file_resubmit',
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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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

# CACHE_BACKEND = "django.core.cache.backends.dummy.DummyCache"
CACHE_BACKEND = 'django.core.cache.backends.filebased.FileBasedCache'
CACHE_LOCATION_DIR = os.path.join(BASE_DIR, 'cache')

# CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'
# CACHE_MAX_ENTRIES = 1000
CACHE_TIMEOUT = 900

# CACHE_BACKEND = 'django.core.cache.backends.memcached.MemcachedCache'
# CACHE_LOCATION = '127.0.0.1:11211'

CACHES = {
    'default': {
        'BACKEND': CACHE_BACKEND,
        'LOCATION': CACHE_LOCATION_DIR,
        'TIMEOUT': CACHE_TIMEOUT,
        'OPTIONS': {
            # 'MAX_ENTRIES': CACHE_MAX_ENTRIES,
        }
    },
    'images': {
        'BACKEND': CACHE_BACKEND,
        'LOCATION': os.path.join(CACHE_LOCATION_DIR, 'images'),
        'TIMEOUT': CACHE_TIMEOUT,
    },
    'file_resubmit': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(CACHE_LOCATION_DIR, 'file_resubmit'),
    },
}


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

TIME_ZONE = 'UTC'

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
# COMPRESS_PRECOMPILERS = (
#     ('text/x-scss', 'django_libsass.SassCompiler'),
# )


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1",
]

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
            'ul'
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
        '360w_poor': {'crop': 'scale', 'size': (360, 360), 'quality': 10, 'bw': True},
        '360w': {'crop': 'scale', 'size': (360, 360), 'quality': 95, },

        '720w_poor': {'crop': 'scale', 'size': (720, 720), 'quality': 10, 'bw': True},
        '720w': {'crop': 'scale', 'size': (720, 720), 'quality': 95, },

        '1080w_poor': {'crop': 'scale', 'size': (1080, 1080), 'quality': 10, 'bw': True},
        '1080w': {'crop': 'scale', 'size': (1080, 1080), 'quality': 95, },

        '1920w_poor': {'crop': 'scale', 'size': (1920, 1920), 'quality': 10, 'bw': True},
        '1920w': {'crop': 'scale', 'size': (1920, 1920), 'quality': 95, },
    }}

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
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

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
