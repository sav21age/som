# Generated by Django 4.1.7 on 2023-09-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_menu_is_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='path_name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='path_namespace',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='slug',
        ),
        migrations.AddField(
            model_name='menu',
            name='url',
            field=models.CharField(blank=True, max_length=100, verbose_name='url-адрес страницы'),
        ),
    ]