# Generated by Django 4.1.7 on 2023-06-11 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('railing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='railing',
            name='portfolio_title',
        ),
    ]
