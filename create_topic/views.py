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
    if request.method == 'POST':
        if 'text_field' in request.POST:
            text_field = request.POST['text_field']  # записываем значение в переменную без браузера
    elif request.method == 'GET':  # присваиваем значение в строке браузера/переменной
        text_field = request.GET['text_field']
    if text_field is not None:
        create = CreatePost(post_text=str(text_field))
        create.save()
    return HttpResponse('Добавлено!')
