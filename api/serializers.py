from rest_framework import serializers
from .models import testing_data_raw, training_data_raw, testing_data_input

class testing_data_raw_serializer(serializers.Serializer):
    precinct = serializers.IntegerField()
    CD = serializers.IntegerField()
    age = serializers.CharField()
    gender = serializers.CharField()
    party = serializers.CharField()

    def create(self, validated_data):
        return testing_data_raw.objects.create(validated_data)
        
    def update(self, instance, validated_data):
        validated_data.precinct = validated_data.get('precinct', instance.precinct)
        validated_data.CD = validated_data.get('CD', instance.CD)
        validated_data.age = validated_data.get('age', instance.age)
        validated_data.gender = validated_data.get('gender', instance.gender)
        validated_data.party = validated_data.get('party', instance.party)
        instance.save()
        return instance

class testing_data_input_serializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    precinct = serializers.IntegerField()
    CD = serializers.IntegerField()
    age = serializers.CharField()
    gender = serializers.CharField()
    party = serializers.CharField()

    def create(self, validated_data):
        return testing_data_input.objects.create(validated_data)
        
    def update(self, instance, validated_data):
        validated_data.user_id = validated_data.get('user_id', instance.user_id)
        validated_data.precinct = validated_data.get('precinct', instance.precinct)
        validated_data.CD = validated_data.get('CD', instance.CD)
        validated_data.age = validated_data.get('age', instance.age)
        validated_data.gender = validated_data.get('gender', instance.gender)
        validated_data.party = validated_data.get('party', instance.party)
        instance.save()
        return instance

class training_data_raw_serializer(serializers.Serializer):
    precinct = serializers.IntegerField()
    CD = serializers.IntegerField()
    age = serializers.CharField()
    gender = serializers.CharField()
    early_vote = serializers.CharField()
    party = serializers.CharField()

    def create(self, validated_data):
        return training_data_raw.objects.create(validated_data)
        
    def update(self, instance, validated_data):
        validated_data.precinct = validated_data.get('precinct', instance.precinct)
        validated_data.CD = validated_data.get('CD', instance.CD)
        validated_data.age = validated_data.get('age', instance.age)
        validated_data.gender = validated_data.get('gender', instance.gender)
        validated_data.early_vote = validated_data.get('early vote', instance.early_vote)
        validated_data.party = validated_data.get('party', instance.party)
        instance.save()
        return instance