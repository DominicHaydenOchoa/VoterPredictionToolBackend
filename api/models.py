from django.db import models
import csv
# Create your models here.

class testing_data_raw(models.Model):
    precinct = models.IntegerField()
    CD = models.IntegerField()
    age = models.CharField(max_length=8)
    gender = models.CharField(max_length=1)
    party = models.CharField(max_length=3)

"""with open('C:/Users/Dominic/Documents/Capstone/HEVM/backend/api/csv/testing_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        testing_data_raw.objects.create(
            precinct = row['Precinct'],
            CD = row['Congressional District'],
            age = row['Age'],
            gender = row['Gender'],
            party = row['Party'], )"""
        
        


