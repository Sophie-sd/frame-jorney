from django.urls import path
from . import views

# app_name = 'core' # Для неймспейсів URL, якщо знадобиться

urlpatterns = [
    path('', views.home, name='home'),
    # Видалені закоментовані шляхи для about, portfolio, reviews, services, contact
] 