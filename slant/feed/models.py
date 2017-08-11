# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, IntegrityError
from django.utils import timezone

import twitter_api

# Create your models here.

class Tweet(models.Model):
  screen_name = models.CharField(max_length=200, default='', null=True)
  tweet_id = models.BigIntegerField(unique=True, null=True)
  html = models.TextField(default='', null=True)
  created_at = models.DateTimeField('date downloaded',
      default=timezone.now, null=True)

  def __str__(self):
    return "{} {}".format(self.screen_name, self.tweet_id)

  @classmethod
  def check_for_new(cls):
    success = False

    query_strings = [
        "from:nytgraphics",
        "from:MarshallProject",
        "from:WSJGraphics",
        "from:jacobinmag",
        "from:NPR",
        ]
    bot = twitter_api.TwitterAPIBot()
    bot.authenticate()

    for q in query_strings:
      tweets = bot.getSearch(q)

      if tweets:
        success = True

        # first, delete old ones (downloaded more than 24 hours ago)
        now = timezone.now()
        for t in Tweet.objects.all():
          if (now - t.created_at).seconds >= 86400:
            t.delete()

        for tweet in tweets:
          t = Tweet(screen_name = tweet.screen_name,
                tweet_id = tweet.id, 
                html = tweet.html)
          try:
            t.save()
          except IntegrityError as e:
            continue

    return success
