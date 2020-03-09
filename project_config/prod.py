'''Use this for production'''

from .base import *

DOMAIN = 'http://domain.com'

DEBUG = False
ALLOWED_HOSTS += [DOMAIN]
CORS_ORIGIN_WHITELIST += [DOMAIN]
WSGI_APPLICATION = 'project_config.wsgi.prod.application'

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'email-smtp.eu-central-1.amazonaws.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.environ.get('AWS_SES_SMTP_USER')
EMAIL_HOST_PASSWORD = os.environ.get('AWS_SES_PASSWORD')
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.environ.get('SENDING_EMAIL')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_URL'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'