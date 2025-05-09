# Generated by Django 4.2.17 on 2025-01-18 09:34

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_remove_profile_headline_profile_short_intro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='images/user-default.webp', max_length=255, verbose_name='image'),
        ),
    ]
