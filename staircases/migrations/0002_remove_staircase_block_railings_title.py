# Generated by Django 4.1.7 on 2023-06-28 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staircases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staircase',
            name='block_railings_title',
        ),
    ]
