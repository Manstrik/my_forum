"""Файл маршрутов приложения users_app."""

from django.urls import path

from users_app.views import logout

app_name = 'users_app'

urlpatterns = [
    # Метод для выхода пользователя
    path(r'logout/', logout, name='logout'),
]
