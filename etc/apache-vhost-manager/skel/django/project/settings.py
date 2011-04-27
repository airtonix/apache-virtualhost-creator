import sys, os

sys.path.insert(0,
	os.path.abspath(
	os.path.normpath('%s/../' % os.path.dirname(__file__))
	)
)

for settings_file in os.listdir( os.path.join(here_path, "settings_d") ) :
	file_name, file_ext = os.path.splitext(settings_file)
	if file_ext != ".pyc" and file_name != "__init__" :
		module_name = "settings_d.%s" % file_name
		try:
			exec("from %s import *" % module_name)
		except ImportError:
			pass

INTERNAL_IPS = ('127.0.0.1',)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

try:
	from settings_d.key import *
except ImportError:
	from hashlib import sha1
	from base.lib.generate_key import generate_key

	secret_key_file = open( os.path.join(PROJECT_ROOT, "settings_d", "key.py"), "w" )
	secret_key_file.write( """secret_key="%s" """ % generate_key( 40, 128, digester=sha1 ))
	secret_key_file.close()

	from settings.key import *

ADMINS = (
	# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
	'default': {
		# Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'ENGINE': 'django.db.backends.%s' % DJANGO_DATABASE_TYPE,
		# Or path to database file if using sqlite3.
		'NAME': DJANGO_DATABASE_NAME,
		# Not used with sqlite3.
		'USER': DJANGO_DATABASE_USERNAME,
		# Not used with sqlite3.
		'PASSWORD': DJANGO_DATABASE_PASSWORD,
		# Set to empty string for localhost. Not used with sqlite3.
		'HOST': DJANGO_DATABASE_HOST,
		# Set to empty string for default. Not used with sqlite3.
		'PORT': DJANGO_DATABASE_PORT,
	}
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE='Australia/Adelaide'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE='en_AU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(SERVER_ROOT,'public_html', 'files')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '%s/files/' % PROJECT_URL

# Absolute path to the directory that holds static files.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SERVER_ROOT, 'public_html', 'static')

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '%s/static/' % PROJECT_URL

# URL prefix for admin media -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# A list of locations of additional static files
STATICFILES_DIRS = (
	os.path.join(SERVER_ROOT,'public_html'),
)

# Make this unique, and don't share it with anybody.
ROOT_URLCONF = 'project.urls'


STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
	os.path.join(PROJECT_ROOT, "templates"),
	os.path.join(PROJECT_ROOT, "base", "templates"),
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'south',
	'project.base',
)


LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler',
		},
		'console':{
			'level':'DEBUG',
			'class':'logging.StreamHandler',
			'formatter': 'simple'
		},

	},
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'loggers': {
		'django.request':{
			'handlers': ['console', 'mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}

