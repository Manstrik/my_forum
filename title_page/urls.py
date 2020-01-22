"""Файл маршрутов приложения title_page."""

from django.urls import path
from django.views.generic import RedirectView

from title_page.views import PostDetail, PostList

app_name = 'title_page'

urlpatterns = [
    # Раздел редиректа
    path('', RedirectView.as_view(url='posts/'), name='index'),
    # Главная страница приложения со списком постов
    path('posts/', PostList.as_view(), name='post-list'),
    # Страница с детальной информацией о посте
    path(r'posts/<int:pk>/', PostDetail.as_view(), name='post-detail')
]
