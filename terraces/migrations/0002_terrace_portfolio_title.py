# Generated by Django 4.1.7 on 2023-07-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terraces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='terrace',
            name='portfolio_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Заголовок'),
        ),
    ]
