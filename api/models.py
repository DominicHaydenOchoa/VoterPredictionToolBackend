from django.db import models
# Create your models here.

class testing_data_raw(models.Model):
    precinct = models.IntegerField()
    CD = models.IntegerField()
    age = models.CharField(max_length=8)
    gender = models.CharField(max_length=1)
    party = models.CharField(max_length=3)