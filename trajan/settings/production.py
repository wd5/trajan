from settings.common import *

DEBUG = False
TEMPLATE_DEBUG =  THUMBNAIL_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Need to modify to seperate from rest of environment?
MEDIA_ROOT = '/'
MEDIA_URL = 'http://static.derek.stegelman.com/media/'

STATIC_ROOT = ''
STATIC_URL = 'http://static.derek.stegelman.com/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.


TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

ROOT_URLCONF = 'urls.production'
#DJANGO_MEMCACHED_REQUIRE_STAFF = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api_docs',
    'grappelli',
    'south',
    'django.contrib.admin',
    
    'locations',
    'core',
    'blog',
    'bookmarks',
    'brew',
    'sorl.thumbnail',
    'hadrian.dist.tagging',
    'tastypie',
    'traveler',
    #'sentry.client',
    #'django_memcached',
    
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/dstegelman/memcached.sock',
    }
}


CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = ''