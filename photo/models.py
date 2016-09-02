from django.db import models

# Create your models here.
class Photo(models.Model):
    url = models.CharField(max_length=250)
    title = models.CharField(max_length=350)
    link = models.CharField(max_length=800)
    data = models.DateTimeField()
    class Meta:
        db_table = 'photo'
        ordering = ['-data']


