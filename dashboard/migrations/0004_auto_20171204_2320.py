# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20171204_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameters',
            name='IPM_file',
            field=models.FileField(default='', upload_to='datasets/'),
        ),
    ]
