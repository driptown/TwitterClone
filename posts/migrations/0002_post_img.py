# Generated by Django 4.1.4 on 2022-12-07 22:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
