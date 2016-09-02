# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=500)),
                ('data', models.DateTimeField()),
            ],
            options={
                'ordering': ['-data'],
                'db_table': 'photo',
            },
        ),
    ]


























































































































