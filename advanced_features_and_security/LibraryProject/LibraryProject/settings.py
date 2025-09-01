# LibraryProject/settings.py
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'  # Replace with environment variable in production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
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

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ================= SECURITY SETTINGS =================
# Add these security configurations at the end of the file

# Browser security headers
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS filter in browsers
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking by denying frame embedding
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing

# Cookie security (set to True in production with HTTPS)
CSRF_COOKIE_SECURE = True  # Send CSRF cookie only over HTTPS
SESSION_COOKIE_SECURE = True  # Send session cookie only over HTTPS

# Additional security settings (recommended for production)
SECURE_SSL_REDIRECT = False  # Set to True in production with HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year - Enable HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include subdomains in HSTS
SECURE_HSTS_PRELOAD = True  # Allow preloading of HSTS

# CSRF settings
CSRF_USE_SESSIONS = False
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'

# Session settings
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# File upload security
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # 2.5MB
FILE_UPLOAD_PERMISSIONS = 0o644
# LibraryProject/settings.py
# Add this to your existing security settings section

# ================= HTTPS & SECURITY CONFIGURATION =================
# Documentation: This section implements comprehensive security measures for HTTPS enforcement
# and protection against common web vulnerabilities.

# HTTPS Enforcement Settings
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=31536000, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True, cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=True, cast=bool)

# Secure Cookie Settings
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)

# Security Headers Configuration
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', default=True, cast=bool)
SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', default=True, cast=bool)

# Additional Security Settings
SECURE_REFERRER_POLICY = 'same-origin'

# SECURE_PROXY_SSL_HEADER: Handle HTTPS detection behind proxies
# This tells Django to trust the X-Forwarded-Proto header that comes from your proxy/load balancer
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Session Security
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True

# CSRF Settings
CSRF_USE_SESSIONS = True
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='', cast=Csv())

# File Upload Security
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # 2.5MB
FILE_UPLOAD_PERMISSIONS = 0o644
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000