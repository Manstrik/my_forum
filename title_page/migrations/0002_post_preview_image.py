# Generated by Django 3.0.2 on 2020-01-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('title_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to='post-images', verbose_name='Картинка на посте'),
        ),
    ]
