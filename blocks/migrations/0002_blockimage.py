# Generated by Django 4.1.7 on 2023-06-14 12:10

import common.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visible', models.BooleanField(db_index=True, default=1, verbose_name='показывать')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='заголовок')),
                ('img_path', models.FileField(blank=True, null=True, upload_to=common.helpers.get_image_path, verbose_name='путь к картинке')),
            ],
            options={
                'verbose_name': 'Блок с картинкой',
                'verbose_name_plural': 'Блоки с картинками',
            },
        ),
    ]
