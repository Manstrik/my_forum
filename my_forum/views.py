"""Общие представления для всего проекта."""

from django.shortcuts import render


def handler404(request, *args, **kwargs):
    """
    Кастомная страница обработки ошибки 404.

    :param request: объект запроса
    :return: отрендеренный шаблон
    """
    return render(request, 'error_pages/404.html')
