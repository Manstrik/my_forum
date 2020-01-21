"""Файл маршрутов приложения title_page."""

from django.urls import path

from title_page.views import IndexView

app_name = 'title_page'

urlpatterns = [
    # Главная страница приложения
    path('', IndexView.as_view(), name='index'),
    path(r'user/<int:pk>/', IndexView.as_view(), name='user-detail')
]
