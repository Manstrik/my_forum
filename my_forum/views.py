"""Общие представления для всего проекта."""

from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'error_pages/404.html', context={'exception': exception})
