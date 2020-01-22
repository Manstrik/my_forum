# Create your models here.

from django.db import models


class CreatePost(models.Model):
    new_post = models.TextField(default=None)
