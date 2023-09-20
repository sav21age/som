# Generated by Django 4.1.7 on 2023-09-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_title', models.CharField(max_length=80, verbose_name='title')),
                ('meta_description', models.CharField(max_length=160, verbose_name='meta description')),
                ('name', models.CharField(max_length=80, verbose_name='h1-название')),
                ('slug', models.SlugField(max_length=80, unique=True, verbose_name='url-адрес страницы')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('is_visible', models.BooleanField(db_index=True, default=1, verbose_name='показывать')),
                ('address_showroom', models.CharField(blank=True, max_length=200, null=True, verbose_name='адрес выставочного зала')),
                ('address_showroom_map', models.TextField(blank=True, null=True, verbose_name='карта проезда до выставочного зала')),
                ('address_production', models.CharField(blank=True, max_length=200, null=True, verbose_name='адрес производства')),
                ('address_production_map', models.TextField(blank=True, null=True, verbose_name='карта проезда к производству')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='телефон')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('work_schedule', models.CharField(blank=True, max_length=50, null=True, verbose_name='график работы')),
            ],
            options={
                'verbose_name': 'контакты',
                'verbose_name_plural': 'контакты',
            },
        ),
    ]
