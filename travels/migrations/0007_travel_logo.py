# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-13 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0006_travel_image4'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='logo',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
