from django.urls import path
from . import views

# Додаємо app_name для неймспейсів, якщо знадобиться
# app_name = 'core'

urlpatterns = [
    # Залишаємо тільки маршрут для головної сторінки
    path('', views.home, name='home'),
    # Видаляємо інші URL-и
    # path('about/', views.about, name='about'),
    # path('portfolio/', views.portfolio, name='portfolio'),
    # path('reviews/', views.reviews, name='reviews'),
    # path('services/', views.services, name='services'),
    # path('contact/', views.contact, name='contact'),
] 