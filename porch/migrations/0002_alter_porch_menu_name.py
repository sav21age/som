# Generated by Django 4.1.7 on 2023-06-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porch',
            name='menu_name',
            field=models.CharField(max_length=80, verbose_name='название для меню'),
        ),
    ]
