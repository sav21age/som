# Generated by Django 4.1.7 on 2023-06-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coeff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h', models.PositiveSmallIntegerField(default=0, verbose_name='коэффициент высоты')),
            ],
            options={
                'verbose_name': 'коэффициент',
                'verbose_name_plural': 'коэффициенты',
            },
        ),
        migrations.CreateModel(
            name='CoeffStaircaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='название')),
                ('price', models.PositiveSmallIntegerField(default=0, verbose_name='цена')),
                ('order_number', models.PositiveSmallIntegerField(default=0, verbose_name='порядковый номер')),
                ('is_visible', models.BooleanField(db_index=True, default=1, verbose_name='показывать')),
            ],
            options={
                'verbose_name': 'Коэффициент для типа лестницы',
                'verbose_name_plural': 'Коэффициенты для типов лестницы',
                'ordering': ['order_number'],
            },
        ),
        migrations.CreateModel(
            name='RailingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='название')),
                ('price', models.PositiveSmallIntegerField(default=0, verbose_name='цена')),
                ('order_number', models.PositiveSmallIntegerField(default=0, verbose_name='порядковый номер')),
                ('is_visible', models.BooleanField(db_index=True, default=1, verbose_name='показывать')),
            ],
            options={
                'verbose_name': 'тип ограждения',
                'verbose_name_plural': 'тип ограждений',
                'ordering': ['order_number'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='название')),
                ('price', models.PositiveSmallIntegerField(default=0, verbose_name='цена')),
                ('order_number', models.PositiveSmallIntegerField(default=0, verbose_name='порядковый номер')),
                ('is_visible', models.BooleanField(db_index=True, default=1, verbose_name='показывать')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'услуги',
                'ordering': ['order_number'],
            },
        ),
        migrations.CreateModel(
            name='StepsMaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='название')),
                ('price', models.PositiveSmallIntegerField(default=0, verbose_name='цена')),
                ('order_number', models.PositiveSmallIntegerField(default=0, verbose_name='порядковый номер')),
                ('is_visible', models.BooleanField(db_index=True, default=1, verbose_name='показывать')),
            ],
            options={
                'verbose_name': 'тип материала ступеней',
                'verbose_name_plural': 'тип материала ступеней',
                'ordering': ['order_number'],
            },
        ),
    ]
