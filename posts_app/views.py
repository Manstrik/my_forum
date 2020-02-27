"""Представления для приложения posts_app."""

from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from lib.utils import multipart_to_dict
from posts_app.models import Post


class PostList(ListView):
    """Класс-представление страницы с постами приложения posts_app."""

    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    """Класс-представление страницы с детальной информацией о посте приложения posts_app."""

    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'


def create_post(request):
    """
    API-функция для создания нового поста.

    :param request: объект запроса
    :return: редирект на страницу с постами
    """
    response = redirect('posts_app:post_list')

    if request.method == 'GET':
        return response

    data = multipart_to_dict(request.POST)

    data['preview_image'] = request.FILES.get('preview_image', None)

    data['created_by'] = request.user

    Post.objects.create(**data)

    return response
