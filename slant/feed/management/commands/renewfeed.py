from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from django.utils import timezone
from feed.models import Tweet
from feed import twitter_api
import os

class Command(BaseCommand):
  help = 'Renews the feed'

  def add_arguments(self, parser):
    parser.add_argument('-q', '--queries',
        nargs='+',
        type=str,
        required=False)

  def handle(self, *args, **options):
    bot = twitter_api.TwitterAPIBot()
    bot.authenticate()
    qlist = options['queries']

    tweets = bot.runSearches(Tweet, qlist=qlist)

    if tweets:
      # first, delete old ones (downloaded more than 24 hours ago)
      now = timezone.now()
      for t in Tweet.objects.all():
        if (now - t.created_at).seconds >= 86400:
          t.delete()

      for tweet in tweets:
        try:
          tweet.save()
        except IntegrityError as e:
          continue

