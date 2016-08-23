from django.db import models

# Create your models here.
class Photo(models.Model):
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    class Meta:
        db_table = 'photo'


