# Generated by Django 4.1.7 on 2023-06-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staircases', '0007_alter_staircasetypicalproject_frame_broken_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staircasetypicalproject',
            name='steps_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='высота ступеней, м'),
        ),
    ]
