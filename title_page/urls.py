"""Файл маршрутов приложения title_page."""

from django.urls import path

from title_page.views import Index

app_name = 'title_page'

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
