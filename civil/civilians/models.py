from django.db import models

# Create your models here.
class Civilians(models.Model):
    nin = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    mother_last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()