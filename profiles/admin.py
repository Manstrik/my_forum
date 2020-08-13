"""Файл админки приложения profiles."""

from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.
app_models = apps.get_app_config('profiles').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
