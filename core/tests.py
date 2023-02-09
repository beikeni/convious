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

    def test_individual_vote_success(self):
        response = self.client.post(reverse('core:vote'), {
            'user': 3,
            'restaurant': 2
        })
        self.assertEqual(response.status_code, 201)

    def test_individual_vote_exceed_daily_limit(self):
        for _ in range(DAILY_VOTE_LIMIT):
            self.client.post(reverse('core:vote'), {
                'user': 5,
                'restaurant': random.randint(1, 10)
            })

        response = self.client.post(reverse('core:vote'), {
            'user': 5,
            'restaurant': 4
        })

        self.assertEqual(response.status_code, 403)

    def test_winner_today(self):
        response = self.client.get(reverse('core:result'))
        self.assertEqual(response.status_code, 200)
