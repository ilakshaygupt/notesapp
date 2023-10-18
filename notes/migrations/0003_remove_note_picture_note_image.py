# Generated by Django 4.2.6 on 2023-10-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='picture',
        ),
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media'),
        ),
    ]