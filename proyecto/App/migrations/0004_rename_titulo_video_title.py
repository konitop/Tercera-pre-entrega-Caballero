# Generated by Django 4.2 on 2023-05-01 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_title_video_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='Titulo',
            new_name='title',
        ),
    ]