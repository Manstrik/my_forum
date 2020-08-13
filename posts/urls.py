"""Файл маршрутов приложения posts."""

from django.urls import path
from django.views.generic import TemplateView

from posts.views import create_post, PostDetail, PostList

app_name = 'posts'

urlpatterns = [
    # Главная страница приложения со списком постов
    path(r'', PostList.as_view(), name='post_list'),
    # Страница с детальной информацией о посте
    path(r'<int:pk>/', PostDetail.as_view(), name='post_detail'),
    # Страница с формой для создания нвого поста
    path(r'new/', TemplateView.as_view(template_name='post_create.html'), name='new_post'),
    # API-функция для создания поста
    path(r'create/', create_post, name='create')
]
