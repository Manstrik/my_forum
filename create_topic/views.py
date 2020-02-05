"""Представления для приложения create_topic."""

from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import CreatePost


class Index(ListView):
    """Класс-представление основной страницы приложения create_topic."""

    template_name = 'create_topic/index.html'
    # Ты передавал неправильную модель в шаблон (скопировал ранее у меня видимо)
    # model = User
    model = CreatePost
    # Аналогично с именем, под которым тебе передается в шаблон
    # context_object_name = 'users'
    context_object_name = 'posts'


def create_post(request):
    """
    Функция для создания поста.

    :param request: обхект запроса
    """
    text_field = None
    text_post_name = None
    if request.method == 'POST':  # если запрос пост, то
        if 'text_field' in request.POST:
            text_field = request.POST['text_field']  # текст поста
            text_post_name = request.POST['post_name']  # название поста
    if request.method == 'GET':  # присваиваем значение в строке браузера/переменной
        text_field = request.GET['text_field']  # текст поста
        text_post_name = request.GET['post_name']  # название поста
    if text_field and text_post_name is not None:
        create_text = CreatePost(post_text=str(text_field),  # сохраняем в базу
                                 post_name=str(text_post_name))
        create_text.save()
    return HttpResponse('Добавлено!')


def loading_postdb(request):
    """
    Здесь должен быть комментарий.

    :param request:
    :return:
    """
    posts = CreatePost.objects.all()  # загружаем все данные из БД
    return render(request, 'create_topic/index.html', locals())  # передаём их в html