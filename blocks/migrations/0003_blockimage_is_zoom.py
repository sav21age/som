# Generated by Django 4.1.7 on 2023-06-14 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0002_blockimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockimage',
            name='is_zoom',
            field=models.BooleanField(default=1, verbose_name='показывать'),
        ),
    ]
