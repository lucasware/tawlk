import djcelery,os

djcelery.setup_loader()

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2', 
        'NAME': 'your_db_name',                      
        'USER': 'your_db_user',                     
        'PASSWORD': 'your_pass',          
    }
}

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(PROJECT_PATH,'media')

MEDIA_URL = '/media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
		os.path.join(PROJECT_PATH,'templates'),
)

INSTALLED_APPS = (
    'djcelery',
    'kral',
)

# What Kral plugins to enable
KRAL_PLUGINS = ['Buzz', 'Identica', 'Twitter', 'Facebook', 'Youtube']
# Minimum amount of time queries will get before rotation happens
KRAL_WAIT = 5
# Maximum number of queries to have running simultaneously
KRAL_SLOTS = 2
# What method Kral uses to communicate
# Valid values: STOMP, AMQP
KRAL_PUSH_METHOD = 'STOMP'

#Celery settings
CELERY_RESULT_BACKEND = "amqp"
CELERY_AMQP_TASK_RESULT_EXPIRES = 18000

#AMPQ Server Info
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672
BROKER_VHOST = "/"
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"

CELERYBEAT_SCHEDULER="djcelery.schedulers.DatabaseScheduler"

ORBITED_SERVER = "localhost"
ORBITED_PORT = "9000"
ORBITED_STOMP_PORT = "61613"

#Load installation specific settings/passwords from external file with restrictive permissions
execfile(os.path.join(PROJECT_PATH,'.private-settings'))


# vim: ai ts=4 sts=4 et sw=4
