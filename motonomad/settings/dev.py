from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '34wr@@_jr@*r@+f%calr4r)+kxq(ui@9e^@m6y6%-0t9_5ya(7'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '/static/jquery/dist/jquery.min.js',
}

INTERNAL_IPS = ['127.0.0.1']

try:
    from .local import *
except ImportError:
    pass

