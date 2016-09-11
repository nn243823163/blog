from __future__ import unicode_literals

from django.db import models

# Create your models here.

class HK_jiaoyisuo(models.Model):
    time_hk = models.TimeField()
    data1 = models.IntegerField()
    data2 = models.IntegerField()
    data3 = models.CharField(max_length=4)
    class Meta:
        db_table = 'hk_jiaoyisuo'
