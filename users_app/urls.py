"""Файл маршрутов приложения users_app."""

from django.urls import path
from django.views.generic import TemplateView

from users_app.views import login, logout

app_name = 'users_app'

urlpatterns = [
    # Метод для выхода пользователя
    path(r'logout/', logout, name='logout'),

    # Метод для выхода пользователя
    path(r'login/', login, name='login'),

    # Страница с формой для входа на сайт
    path(r'login-page/', TemplateView.as_view(template_name='login_page.html'), name='login_page'),
]
