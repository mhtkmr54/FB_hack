import os

TIME_ZONE = 'Asia/Calcutta'
LANGUAGE_CODE = 'en-us'


SITE_ID = 1

USE_I18N = False

USE_L10N = True


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'dajaxice',
    'dajax',
    'users',
    'likes',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.request",
"django.contrib.messages.context_processors.messages",
"context_processors.site_url",)

DAJAX_JS_FRAMEWORK = "jQuery"
DAJAX_MEDIA_PREFIX='dajax'
DAJAXICE_MEDIA_PREFIX="dajaxice"
DAJAXICE_DEBUG = True

CACHES = {
        'default': {
                    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                            'LOCATION': '127.0.0.1:11211',
                                }
}

RECAPTCHA_PUBLIC_KEY = '6Lf1ktUSAAAAALOtemzm08LVwHmfku6yXXCdrMJn'
RECAPTCHA_PRIVATE_KEY = '6Lf1ktUSAAAAANLvSSLPiSpgocDrjyK9ApPUvcaF'