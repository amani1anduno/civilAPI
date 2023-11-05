from django.db import models

# Create your models here.
class Custody(models.Model):
    nin = models.IntegerField(primary_key=True)
    