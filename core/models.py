from typing import Set, Dict

from django.contrib.auth import get_user_model
from django.db import models
import datetime

DAILY_VOTE_LIMIT = 5


class DailyVoteCountExceededError(Exception):
    pass


class Restaurant(models.Model):
    name = models.CharField(max_length=50)


class Vote(models.Model):
    date = models.DateField(unique=True, db_index=True)
    result = models.JSONField(null=True)

    class Meta:
        ordering = ['-date']

    @staticmethod
    def calculate_score(single_user_vote_count: int) -> float:
        """
        :param single_user_vote_count: Int
        :return: Weighted value of votes
        """
        if single_user_vote_count == 1:
            return 1
        if single_user_vote_count == 2:
            return 1.5
        else:
            return 1.5 + ((single_user_vote_count - 2) * 0.25)

    def get_restaurants(self) -> Set:
        """
        :return: Set containing restaurants that appear in a given voting session
        """
        return set([individual_vote.restaurant for individual_vote in self.individual_votes.all()])

    def get_users(self) -> Set:
        """
        :return: Set containing distinct users who in a given voting session
        """
        return set([individual_vote.user for individual_vote in self.individual_votes.all()])

    def get_restaurant_users(self, restaurant: Restaurant) -> Set:
        """
        :param restaurant: Restaurant
        :return: Set containing distinct users who voted for a given restaurant in a given voting session
        """
        return set([individual_vote.user for individual_vote in self.individual_votes.filter(restaurant=restaurant)])

    def process_vote(self) -> None:
        """
        Stores results in JSON Field `result`
        :return: None
        """
        result = []

        for index, restaurant in enumerate(self.get_restaurants()):
            result.append({
                'restaurant_id': restaurant.id,
                'restaurant_name': restaurant.name,
                'score': 0.0,
                'distinct_users': len(self.get_restaurant_users(restaurant))
            })

            for user in self.get_restaurant_users(restaurant=restaurant):
                single_user_vote_count: int = IndividualVote.objects.filter(restaurant=restaurant, user=user).count()
                result[index]['score'] += self.calculate_score(single_user_vote_count)

        self.result = result
        self.save()

    def get_winner(self) -> Dict:
        """
        :return: Dict object containing winning restaurant for a given vote
        """
        max_score = max(self.result, key=lambda item: item['score'])
        winners = [restaurant for restaurant in self.result if restaurant['score'] == max_score['score']]
        tie = True if len(winners) > 1 else False
        if tie:
            return max(winners, key=lambda item: item['distinct_users'])
        return winners[0]


class IndividualVote(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="individual_votes")
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name="individual_votes")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="individual_votes")
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_vote_count(cls, user: get_user_model(), date: datetime.date) -> int:
        """
        :param user: User
        :param date: Datetime.date
        :return: Vote count per user per given date
        """
        return cls.objects.filter(user=user, vote__date=date).count()

    @classmethod
    def register(cls, user: get_user_model(), restaurant: Restaurant, date: datetime.date) -> None:
        """
        :param user: User
        :param restaurant: Restaurant
        :param date: Datetime.date
        :return: None if vote registered correctly or raises DailyVoteCountExceededError if user daily vote count exceeded
        """
        if cls.get_vote_count(user=user, date=date) < DAILY_VOTE_LIMIT:
            vote, _ = Vote.objects.get_or_create(date=date)
            cls.objects.create(user=user, vote=vote, restaurant=restaurant)
        else:
            raise DailyVoteCountExceededError
