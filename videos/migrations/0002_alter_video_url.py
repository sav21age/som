# Generated by Django 4.1.7 on 2023-06-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(max_length=255, verbose_name='ссылка'),
        ),
    ]