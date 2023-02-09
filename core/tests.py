import datetime
import random

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from core.models import IndividualVote, Restaurant, DAILY_VOTE_LIMIT, Vote


def vote(user, restaurant):
    IndividualVote.objects.create(user=get_user_model().objects.get(id=user),
                                  restaurant=Restaurant.objects.get(id=restaurant))


class TestVoting(TestCase):

    @classmethod
    def setUpTestData(cls):
        call_command('seed')

    def setUp(self):
        self.client = APIClient()
        self.today = datetime.date.today()
        self.users = [user.id for user in get_user_model().objects.all()]
        self.restaurants = [restaurant.id for restaurant in Restaurant.objects.all()]

    def test_individual_vote_success(self):
        response = self.client.post(reverse('core:vote'), {
            'user': random.choice(self.users),
            'restaurant': random.choice(self.restaurants)
        })
        self.assertEqual(response.status_code, 201)

    def test_individual_vote_exceed_daily_limit(self):
        user_id = random.choice(self.users)
        restaurant_id = random.choice(self.restaurants)
        for _ in range(DAILY_VOTE_LIMIT):
            self.client.post(reverse('core:vote'), {
                'user': user_id,
                'restaurant': restaurant_id
            })

        response = self.client.post(reverse('core:vote'), {
            'user': user_id,
            'restaurant': restaurant_id
        })

        self.assertEqual(response.status_code, 403)

    def test_winner_today(self):
        response = self.client.get(reverse('core:result'))
        self.assertEqual(response.status_code, 200)
