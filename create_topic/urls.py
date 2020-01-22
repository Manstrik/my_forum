"""Файл маршрутов приложения create_topic."""

from django.urls import path

from .views import Index

app_name = 'create_topic'

urlpatterns = [
    # Главная страница приложения
    path('', Index.as_view(), name='index'),
    path(r'user/<int:pk>/', Index.as_view(), name='user-detail'),
]
