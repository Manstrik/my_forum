# Generated by Django 3.0.2 on 2020-02-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_user_name',
                 models.CharField(default='Не задано имя', max_length=128, verbose_name='Имя пользователя')),
                ('post_name',
                 models.CharField(default='Не задано имя поста', max_length=128, verbose_name='Тема поста')),
                ('post_text', models.TextField(default='Текст не введён', verbose_name='Текст поста')),
                ('post_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время поста')),
            ],
        ),
    ]
