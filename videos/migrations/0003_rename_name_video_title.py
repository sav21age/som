# Generated by Django 4.1.7 on 2023-05-31 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_alter_video_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='title',
        ),
    ]