# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160823173927 on 2016-08-28 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_auto_20160828_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='link',
            field=models.CharField(max_length=800),
        ),
    ]
