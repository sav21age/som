# Generated by Django 4.1.7 on 2023-06-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0003_alter_blocksvg_block_name'),
        ('terraces', '0003_alter_terrace_block_railings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terrace',
            name='block_railings',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='+', to='blocks.blockimage', verbose_name='объекты'),
        ),
        migrations.AlterField(
            model_name='terrace',
            name='description_text',
            field=models.TextField(blank=True, verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='terrace',
            name='description_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='terrace',
            name='hwaw',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='+', to='blocks.blocksvg', verbose_name='объекты'),
        ),
    ]
