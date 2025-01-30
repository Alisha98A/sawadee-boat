"""
Django settings for sawadee_dining_boat project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1','localhost','.herokuapp.com', '8000-alisha98a-sawadeeboat-05tfwdet2yb.ws-eu117.gitpod.io']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'cloudinary',
    'cloudinary_storage',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reservations',
    'info',
    'accounts',
]

SITE_ID = 1

# Allauth settings for email authentication
LOGIN_REDIRECT_URL = '/accounts/profile/' 
LOGOUT_REDIRECT_URL = '/' 
ACCOUNT_EMAIL_VERIFICATION = 'none'  
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATED_REDIRECT_URL = '/'  
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = 'smtp.mail.me.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('ICLOUD_EMAIL_USER')  
EMAIL_HOST_PASSWORD = os.getenv('ICLOUD_EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

ROOT_URLCONF = 'sawadee_dining_boat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[TEMPLATES_DIR],
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

WSGI_APPLICATION = 'sawadee_dining_boat.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com",
    "https://8000-alisha98a-sawadeeboat-05tfwdet2yb.ws-eu117.gitpod.io"
]


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
