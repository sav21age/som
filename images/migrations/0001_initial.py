# Generated by Django 4.1.7 on 2023-05-26 10:55

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('path', easy_thumbnails.fields.ThumbnailerImageField(blank=True, max_length=200, upload_to=images.models.get_image_path, verbose_name='Путь к картинке')),
                ('alt', models.CharField(blank=True, max_length=200, null=True, verbose_name='аттрибут alt')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='аттрибут title')),
                ('order_number', models.PositiveSmallIntegerField(default=0, verbose_name='порядковый номер')),
                ('is_visible', models.BooleanField(db_index=True, default=1, verbose_name='показывать')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'картинка',
                'verbose_name_plural': 'картинки',
                'ordering': ('order_number',),
            },
        ),
    ]
