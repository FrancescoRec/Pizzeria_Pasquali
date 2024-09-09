from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "your-production-secret-key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['your-production-domain.com', 'www.your-production-domain.com']

# Database (PostgreSQL Example)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Additional production-specific settings, e.g., security
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS
