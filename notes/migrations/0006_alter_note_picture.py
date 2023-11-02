# Generated by Django 4.2.6 on 2023-11-02 13:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_note_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image/'),
        ),
    ]