"""Представления для приложения create_topic."""

from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.views.generic import ListView

from .models import CreatePost


class Index(ListView):
    """Класс-представление основной страницы приложения create_topic."""

    template_name = 'create_topic/index.html'
    model = User
    context_object_name = 'users'


def create_post(request):
    """
    Функция для создания поста.

    :param request: обхект запроса
    """
    text_field = None
    text_post_name = None
    if request.method == 'POST':
        if 'text_field' in request.POST:
            text_field = request.POST['text_field']  # записываем значение в переменную без браузера
            text_post_name = request.POST['post_name']
    if request.method == 'GET':  # присваиваем значение в строке браузера/переменной
        text_field = request.GET['text_field']
        text_post_name = request.GET['post_name']
    if text_field and text_post_name is not None:
        create_text = CreatePost(post_text=str(text_field))
        create_post_name = CreatePost(post_name=str(text_post_name))
        create_text.save()
        create_post_name.save()
    return HttpResponse('Добавлено!')
