# Generated by Django 4.1.7 on 2023-07-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_index_portfolio_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='block_price_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Заголовок'),
        ),
    ]
