"""Файл маршрутов приложения profiles."""

from django.urls import path
from django.views.generic import TemplateView

from profiles.views import login, logout

app_name = 'profiles'

urlpatterns = [
    # Метод для выхода пользователя
    path(r'logout/', logout, name='logout'),

    # Метод для выхода пользователя
    path(r'login/', login, name='login'),

    # Страница с формой для входа на сайт
    path(r'login-page/', TemplateView.as_view(template_name='login_page.html'), name='login_page'),
]
