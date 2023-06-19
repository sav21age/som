# Generated by Django 4.1.7 on 2023-06-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terraces', '0007_remove_terracetypicalproject_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='terracetypicalproject',
            name='frame_length',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='длина, мм'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terracetypicalproject',
            name='frame_thickness',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='толщина, мм'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='terracetypicalproject',
            name='frame_width',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='ширина, мм'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='terracetypicalproject',
            name='height',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='высота, м'),
        ),
        migrations.AlterField(
            model_name='terracetypicalproject',
            name='length',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='длина, м'),
        ),
        migrations.AlterField(
            model_name='terracetypicalproject',
            name='width',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='ширина, м'),
        ),
    ]
