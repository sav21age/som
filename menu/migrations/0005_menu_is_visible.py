# Generated by Django 4.1.7 on 2023-09-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_menu_app_name_menu_path_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_visible',
            field=models.BooleanField(default=1, verbose_name='показывать'),
        ),
    ]