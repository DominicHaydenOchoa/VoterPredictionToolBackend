from django.db import models
import random
import csv
# Create your models here.


class testing_data_raw(models.Model):
    precinct = models.IntegerField()
    CD = models.IntegerField()
    age = models.CharField(max_length=8)
    gender = models.CharField(max_length=1)
    party = models.CharField(max_length=3)

class training_data_raw(models.Model):
    precinct = models.IntegerField()
    CD = models.IntegerField()
    age = models.CharField(max_length=8)
    gender = models.CharField(max_length=1)
    early_vote = models.CharField(max_length=8)
    party = models.CharField(max_length=3)

class testing_data_input(models.Model):
    user_id = models.IntegerField()
    precinct = models.IntegerField()
    CD = models.IntegerField()
    age = models.CharField(max_length=8)
    gender = models.CharField(max_length=1)
    early_vote = models.CharField(max_length=8)
    party = models.CharField(max_length=3)


def model_create_prompt():
    pass

def insert_testing_raw_model():
    with open('C:/Users/Dominic/Documents/Capstone/HEVM/backend/api/csv/testing_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            testing_data_raw.objects.create(
            precinct = row['Precinct'],
            CD = row['Congressional District'],
            age = row['Age'],
            gender = row['Gender'],
            party = row['Party'], )
    



def insert_training_data_raw():
    with open('C:/Users/Dominic/Documents/Capstone/HEVM/backend/api/csv/training_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            training_data_raw.objects.create(
                precinct = row['Precinct'],
                CD = row['Congressional District'],
                age = row['Age'],
                gender = row['Gender'],
                early_vote = row['Early Vote'],
                party = row['Party'] 
        )


