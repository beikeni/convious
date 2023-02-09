from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import IndividualVote


@receiver(post_save, sender=IndividualVote)
def send_email(sender, instance, created, **kwargs):
    instance.vote.process_vote()