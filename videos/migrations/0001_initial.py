# Generated by Django 4.1.7 on 2023-09-21 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('url', models.CharField(max_length=255, verbose_name='ссылка')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='аттрибут title')),
                ('order_number', models.PositiveSmallIntegerField(default=0, verbose_name='порядковый номер')),
                ('is_visible', models.BooleanField(db_index=True, default=1, verbose_name='показывать')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'видео',
                'ordering': ('order_number',),
            },
        ),
    ]
