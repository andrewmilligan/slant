from __future__ import unicode_literals
from django.db import models, IntegrityError
from django.utils import timezone
import json
import os

from local_stories_loader import LocalStoriesLoader

# Create your models here.

class Image(models.Model):
  src = models.URLField(default='')
  caption = models.TextField(default='', null=True)
  provider = models.CharField(max_length=200, default='', null=True)
  producer = models.CharField(max_length=200, default='', null=True)
  copyright = models.CharField(max_length=200, default='', null=True)
  crop_standard_src = models.URLField(default='', null=True)
  crop_square_src = models.URLField(default='', null=True)
  crop_wide_src = models.URLField(default='', null=True)
  crop_enlargement_src = models.URLField(default='', null=True)
  crop_custom_src = models.URLField(default='', null=True)


class PullQuote(models.Model):
  text = models.TextField(default='')
  person = models.CharField(max_length=200, default='', null=True)

  def __unicode__(self):
    return self.text


class Story(models.Model):
  title = models.CharField(max_length=200, default='', unique=True)
  teaser = models.TextField(default='')
  story_date = models.DateTimeField('date published',
      default=timezone.now, null=True)
  byline = models.TextField(default='', null=True)
  text = models.TextField(default='')
  creation_date = models.DateTimeField('datetime downloaded',
      default=timezone.now)
  outlet = models.CharField(max_length=200,default='')
  images = models.TextField(default='')
  pull_quotes = models.ManyToManyField(PullQuote)

  def __unicode__(self):
    return self.title.encode('ascii', 'ignore')

  def bylineName(self):
    return self.byline

  def primaryImage(self):
    img = None
    imgs = json.loads(self.images)
    if imgs:
      img = imgs[0]
    return img

  def imageList(self):
    return json.loads(self.images)

  def storyDateString(self):
    return self.story_date.strftime("%B %d, %Y")

  def storyTimeString(self):
    return self.story_date.strftime("%H:%M %p %Z")
