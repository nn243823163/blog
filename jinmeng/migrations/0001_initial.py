# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160912095645 on 2016-09-13 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HK_jiaoyisuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_hk', models.TimeField()),
                ('data1', models.IntegerField()),
                ('data2', models.IntegerField()),
                ('data3', models.CharField(max_length=4)),
                ('save_data', models.DateTimeField(default=1473773069.55863)),
            ],
            options={
                'db_table': 'hk_jiaoyisuo',
                'verbose_name': '\u9999\u6e2f\u4ea4\u6613\u6240',
                'indexes': [],
            },
        ),
    ]
