from rest_framework import serializers
from .models import testing_data, training_data, testing_data_input, testing_data_result

class testing_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = testing_data
        fields = ['precinct', 'CD', 'age', 'gender', 'early_vote', 'party' ]

class testing_data_input_serializer(serializers.ModelSerializer):
    class Meta:
        model = testing_data_input
        fields = ['session_id', 'precinct', 'CD', 'age', 'gender', 'early_vote', 'party']

class testing_data_result_serializer(serializers.ModelSerializer):
    class Meta:
        model = testing_data_result
        fields = ['session_id', 'precinct', 'CD', 'age', 'gender', 'early_vote',
        'early_vote_score', 'accuracy_result', 'party']

class training_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = training_data
        fields = ['precinct', 'CD', 'age', 'gender', 'early_vote', 'party']
