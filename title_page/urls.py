"""Файл маршрутов приложения title_page."""

from django.urls import path

from title_page.views import Index

app_name = 'title_page'

urlpatterns = [
    # Главная страница приложения
    path('', Index.as_view(), name='index'),
]
