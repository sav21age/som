# Generated by Django 4.1.7 on 2023-06-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terraces', '0010_rename_flooring_terracetypicalproject_flooring_material_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terracetypicalproject',
            name='flooring_material',
            field=models.CharField(max_length=250, verbose_name='материал настила'),
        ),
    ]
