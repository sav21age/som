# Generated by Django 4.1.7 on 2023-06-08 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_remove_index_meta_keywords_alter_index_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='prices',
            new_name='block_price',
        ),
    ]
