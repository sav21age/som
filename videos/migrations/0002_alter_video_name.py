# Generated by Django 4.1.7 on 2023-05-31 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='название'),
        ),
    ]
