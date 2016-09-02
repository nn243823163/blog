from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 30)
    headImg = models.ImageField(upload_to = './test_upload/')

    def __unicode__(self):
        return self.username