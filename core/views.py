import datetime

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import IndividualVote, Vote, DailyVoteCountExceededError, Restaurant
from core.serializers import IndividualVoteSerializer, ResultRequestSerializer, ResultResponseSerializer


class VoteAPIView(APIView):
    serializer_class = IndividualVoteSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_model().objects.get(id=serializer.data['user'])
        restaurant = Restaurant.objects.get(id=serializer.data['restaurant'])

        try:
            IndividualVote.register(user=user, restaurant=restaurant, date=datetime.date.today())
        except DailyVoteCountExceededError:
            return Response({'Error': 'Daily vote count exceeded for this user'}, status=status.HTTP_403_FORBIDDEN)

        return Response({'Success': 'Vote successfully registered'}, status=status.HTTP_201_CREATED)


class ResultAPIView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = ResultRequestSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)

        date = serializer.data['date']
        period_length = serializer.data['period_length']

        start_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        end_date = start_date + datetime.timedelta(days=period_length)

        response = ResultResponseSerializer([{'date': vote.date, 'winner': vote.get_winner()} for vote in
                                             Vote.objects.filter(date__gte=start_date, date__lte=end_date)], many=True)

        return Response(response.data, status=status.HTTP_200_OK)
