from .base import *
import os
# import dj_database_url # Для конфігурації бази даних з URL (напр., Heroku)

# Налаштування для production

DEBUG = False

# !!! ВАЖЛИВО ДЛЯ PRODUCTION !!!
# Переконайтеся, що ці налаштування коректно встановлені перед деплоєм!

# SECRET_KEY та ALLOWED_HOSTS потрібно брати з оточення (environment variables)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY) # Використовуємо базовий ключ як запасний, якщо змінна не встановлена
# !! ОБОВ'ЯЗКОВО встановіть змінну середовища DJANGO_SECRET_KEY на вашому сервері !!

# Приклад отримання ALLOWED_HOSTS з env (розділених комою)
# ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
ALLOWED_HOSTS = [] # !! ОБОВ'ЯЗКОВО заповніть список дозволених хостів (домен вашого сайту) !!

# TODO: Налаштувати базу даних для production (наприклад, PostgreSQL)
# DATABASES = {
#     'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
# }

# WhiteNoise для обслуговування статичних файлів
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware') # Вставити після SecurityMiddleware
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Директорія для збору статичних файлів командою collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'

# TODO: Налаштувати безпеку (HTTPS, HSTS, CSRF_COOKIE_SECURE, SESSION_COOKIE_SECURE і т.д.)
# !! ОБОВ'ЯЗКОВО розкоментуйте та налаштуйте ці параметри для HTTPS !!
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True 