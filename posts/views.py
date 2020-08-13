"""Представления для приложения posts."""

from django.shortcuts import redirect
from django.views.generic import DetailView, ListView

from lib.utils import multipart_to_dict
from posts.models import Post


class PostList(ListView):
    """Класс-представление страницы с постами приложения posts."""

    template_name = 'post_list.html'
    queryset = Post.objects.select_related('author')
    context_object_name = 'posts'


class PostDetail(DetailView):
    """Класс-представление страницы с детальной информацией о посте приложения posts."""

    template_name = 'post_detail.html'
    queryset = Post.objects.select_related('author')
    context_object_name = 'post'


def create_post(request):
    """
    API-функция для создания нового поста.

    :param request: объект запроса
    :return: редирект на страницу с постами
    """
    response = redirect('posts:post_list')

    if request.method == 'GET':
        return response

    data = multipart_to_dict(request.POST)

    data['preview_image'] = request.FILES.get('preview_image', None)

    data['author'] = request.user

    print(data)

    Post.objects.create(**data)

    return response
