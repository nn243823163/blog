from __future__ import unicode_literals
from django.db import models
import time

# Create your models here.

class HK_jiaoyisuo(models.Model):
    time_hk = models.TimeField()
    data1 = models.IntegerField()
    data2 = models.IntegerField()
    data3 = models.CharField(max_length=4)
    save_data = models.DateTimeField(default=time.time())
    class Meta:
        db_table = 'hk_jiaoyisuo'
    def __str__(self):
        return str(self.data2)
