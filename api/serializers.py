from rest_framework import serializers
from .models import testing_data_raw, training_data_raw, testing_data_input

class testing_data_raw_serializer(serializers.ModelSerializer):
    class Meta:
        model = testing_data_raw
        fields = ['precinct', 'CD', 'age', 'gender', 'party' ]

class testing_data_input_serializer(serializers.ModelSerializer):
    class Meta:
        model = testing_data_input
        fields = ['user_id', 'precinct', 'CD', 'age', 'gender', 'early_vote', 'party']

class training_data_raw_serializer(serializers.ModelSerializer):
    class Meta:
        model = training_data_raw
        fields = ['precinct', 'CD', 'age', 'gender', 'early_vote', 'party']