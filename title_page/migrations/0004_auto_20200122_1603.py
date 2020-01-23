# Generated by Django 3.0.2 on 2020-01-22 13:03

import title_page.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('title_page', '0003_auto_20200122_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to=title_page.utils.get_post_image_upload_path,
                                    verbose_name='Картинка на посте'),
        ),
    ]