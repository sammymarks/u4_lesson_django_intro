# Generated by Django 4.2.7 on 2023-11-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0003_song_album_song_preview_url_song_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='preview_url',
        ),
    ]
