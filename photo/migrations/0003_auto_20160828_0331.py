# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160823173927 on 2016-08-28 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20160828_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='link',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.CharField(max_length=150),
        ),
    ]
