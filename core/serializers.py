import datetime

from rest_framework import serializers

from core.models import Vote, IndividualVote, Restaurant


class IndividualVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualVote
        fields = ['user', 'restaurant']


class ResultRequestSerializer(serializers.Serializer):
    date = serializers.DateField(required=False, default=datetime.date.today())
    period_length = serializers.IntegerField(required=False, default=0)


class ResultResponseSerializer(serializers.Serializer):
    date = serializers.DateField()
    winner = serializers.DictField()


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']
