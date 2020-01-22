"""Файл маршрутов приложения posts_app."""

from django.urls import path

from posts_app.views import PostDetail, PostList

app_name = 'posts_app'

urlpatterns = [
    # Главная страница приложения со списком постов
    path('', PostList.as_view(), name='post-list'),
    # Страница с детальной информацией о посте
    path(r'<int:pk>/', PostDetail.as_view(), name='post-detail')
]
