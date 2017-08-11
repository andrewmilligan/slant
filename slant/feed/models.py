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
