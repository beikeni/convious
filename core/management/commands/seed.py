from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
import random

import datetime

from core.models import Restaurant, IndividualVote, DAILY_VOTE_LIMIT, Vote


def populate_past_votes():
    start_date = datetime.datetime.strptime('2023-01-01', "%Y-%m-%d").date()
    days = datetime.date.today() - start_date
    for index in range(days.days):
        current_date = start_date + datetime.timedelta(days=index)
        vote = Vote.objects.create(date=current_date)
        for user in get_user_model().objects.all():
            for _ in range(DAILY_VOTE_LIMIT - 1):
                user_vote(user=user.id, restaurant=random.randint(1, 10), vote=vote)


def user_vote(user, restaurant, vote):
    try:
        IndividualVote.objects.create(user=get_user_model().objects.get(id=user),
                                      restaurant=Restaurant.objects.get(id=restaurant),
                                      vote=vote)
    except Exception as e:
        print(e)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for index in range(1, 11):
            Restaurant.objects.update_or_create(
                name=f"Restaurant {index}",
                defaults={
                    "name": f"Restaurant {index}"
                }
            )
            get_user_model().objects.update_or_create(
                username=f"username{index}",
                defaults={
                    "username": f"username{index}"
                }
            )
        populate_past_votes()
