from .base import *

# Налаштування для розробки

DEBUG = True

ALLOWED_HOSTS = [] # Можна залишити порожнім для локальної розробки

# Використовуємо SQLite для простоти
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Можна додати інші інструменти для розробки, наприклад, django-debug-toolbar
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
# INTERNAL_IPS = ['127.0.0.1'] 