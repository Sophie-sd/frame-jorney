from .base import *
import os
import dj_database_url # Додаємо імпорт

# Налаштування для production

# Визначаємо DEBUG:
# 1. Перевіряємо змінну середовища DEBUG (для ручного ввімкнення на Render)
# 2. Якщо її немає, перевіряємо відсутність змінної RENDER (стандартно для Render)
DEBUG_ENV = os.environ.get('DEBUG', 'False').lower()
if DEBUG_ENV in ('true', '1', 't'):
    DEBUG = True
else:
    DEBUG = 'RENDER' not in os.environ # Стандартна перевірка Render

# !!! ВАЖЛИВО ДЛЯ PRODUCTION !!!
# Переконайтеся, що ці налаштування коректно встановлені перед деплоєм!

# SECRET_KEY беремо з оточення
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)
# !! ОБОВ'ЯЗКОВО встановіть змінну середовища DJANGO_SECRET_KEY на вашому сервері !!

# Налаштовуємо ALLOWED_HOSTS для Render
ALLOWED_HOSTS = [
    "frame-jorney.online",
    "www.frame-jorney.online",
]
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Налаштування бази даних PostgreSQL через DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(
        # Використовуємо базову SQLite як запасний варіант, якщо DATABASE_URL не задано
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600 # Рекомендовано для постійних з'єднань
    )
}


# WhiteNoise для обслуговування статичних файлів
# Переконуємось, що він додається ПІСЛЯ SecurityMiddleware
# Це вже зроблено в base.py, якщо MIDDLEWARE визначено там. Якщо ні - розкоментувати:
MIDDLEWARE.insert(MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Налаштування статичних файлів для production (коли DEBUG=False)
# Ці налаштування тепер будуть застосовані автоматично, коли DEBUG стане False
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Налаштування безпеки (HTTPS, HSTS...) - розкоментувати та налаштувати на Render
# !! ОБОВ'ЯЗКОВО розкоментуйте та налаштуйте ці параметри для HTTPS !!
# SECURE_SSL_REDIRECT = True # Render автоматично обробляє SSL, можливо, це не потрібно
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # Важливо для визначення HTTPS за проксі Render
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True 