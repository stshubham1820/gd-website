from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r@br&(g@o)$^sr4rhcniz=r8&!vz7b$1pe1fax+f$k4pq%&(27'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gd_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gd_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Development settings
STATIC_URL = '/static/'

# Media files settings
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
        BASE_DIR / "static",  # Additional static files can be stored here in development
    ]
# Collect static files here when running `collectstatic`
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files location on the server (development or local testing)
MEDIA_ROOT = BASE_DIR / 'media'

# if os.environ.get('PRODUCTION'):
#     # Production settings
#     STATIC_URL = '/static/'

#     # Media files (uploaded by users) settings
#     MEDIA_URL = '/media/'

#     # Directory for static files (optional: for development)
#     STATICFILES_DIRS = [
#         BASE_DIR / "static",  # Additional static files can be stored here in development
#     ]

#     # Location for collected static files during production (for `collectstatic` command)
#     STATIC_ROOT = BASE_DIR / "staticfiles"

#     # Media files location
#     MEDIA_ROOT = BASE_DIR / "media"

# else:
#     # Development settings
#     STATIC_URL = '/static/'

#     # Media files settings
#     MEDIA_URL = '/media/'

#     # Collect static files here when running `collectstatic`
#     STATIC_ROOT = BASE_DIR / 'staticfiles'

#     # Media files location on the server (development or local testing)
#     MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
