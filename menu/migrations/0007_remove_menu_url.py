# Generated by Django 4.1.7 on 2023-09-20 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_remove_menu_path_name_remove_menu_path_namespace_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='url',
        ),
    ]
