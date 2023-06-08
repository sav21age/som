# Generated by Django 4.1.7 on 2023-06-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staircase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_title', models.CharField(max_length=80, verbose_name='title')),
                ('meta_description', models.CharField(max_length=160, verbose_name='meta description')),
                ('name', models.CharField(max_length=80, verbose_name='h1-название')),
                ('slug', models.SlugField(max_length=80, unique=True, verbose_name='url-адрес страницы')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата обновления')),
                ('is_visible', models.BooleanField(db_index=True, default=1, verbose_name='показывать')),
                ('description_title', models.CharField(blank=True, max_length=200, verbose_name='Заголовок')),
                ('description_text', models.TextField(blank=True, verbose_name='Текст')),
                ('menu_name', models.CharField(max_length=80, verbose_name='название для меню')),
                ('menu_order', models.PositiveSmallIntegerField(default=0, verbose_name='порядковый номер в меню')),
                ('portfolio_title', models.CharField(blank=True, max_length=200, verbose_name='Заголовок')),
                ('block_svg_title', models.CharField(blank=True, max_length=200, verbose_name='Заголовок')),
                ('block_price', models.ManyToManyField(blank=True, db_index=True, related_name='+', to='blocks.blockprice', verbose_name='"Цены"')),
                ('block_svg', models.ManyToManyField(blank=True, db_index=True, related_name='block_svg', to='blocks.blocksvg', verbose_name='"Контент"')),
                ('hwaw', models.ManyToManyField(blank=True, db_index=True, related_name='+', to='blocks.blocksvg', verbose_name='"Как мы работаем?"')),
            ],
            options={
                'verbose_name': 'лестницу',
                'verbose_name_plural': 'лестницы',
                'ordering': ('menu_order',),
            },
        ),
    ]
