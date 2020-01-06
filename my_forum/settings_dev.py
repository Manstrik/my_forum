"""Файл настройка для dev-режима."""

import os

from .settings import BASE_DIR, DATABASES

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
