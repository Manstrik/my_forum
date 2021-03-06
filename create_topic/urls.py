"""Файл маршрутов приложения create_topic."""

from django.conf.urls import url
from django.urls import path

from . import views
from .views import Index, CreatePostPage

app_name = 'create_topic'

urlpatterns = [
    # Главная страница приложения
    path('', Index.as_view(), name='index'),
    path(r'new_post/', CreatePostPage.as_view(), name='creating_posts'),
    path(r'user/<int:pk>/', Index.as_view(), name='user-detail'),
    url('create_post', views.create_post, name='create_post'),
    url('search_post', views.SearchPostsInDB.searching_in_db, name='search_post'),

]
