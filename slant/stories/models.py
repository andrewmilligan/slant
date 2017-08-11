from __future__ import unicode_literals
from django.db import models, IntegrityError
from django.utils import timezone
import json

import npr_api

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
  images = models.ManyToManyField(Image)
  pull_quotes = models.ManyToManyField(PullQuote)

  def __unicode__(self):
    return self.title.encode('ascii', 'ignore')

  def bylineName(self):
    return json.loads(self.byline)[0]['name']['$text']

  def primaryImage(self):
    ret = None
    img_list = self.images.all()
    if img_list:
      ret = img_list[0]
    return ret

  def storyDateString(self):
    return self.story_date.strftime("%B %d, %Y")

  def storyTimeString(self):
    return self.story_date.strftime("%H:%M %p %Z")

  @classmethod
  def check_for_new(cls):
    success = False

    bot = npr_api.NPRAPIBot()
    stories = bot.getNewsStories()

    if stories:
      success = True

      for story in stories:
        images = []
        for img in story.images:
          i = Image(src = img.src,
                    caption = img.caption,
                    provider = img.provider,
                    producer = img.producer,
                    copyright = img.copyright,
                    crop_standard_src = img.crop_standard_src,
                    crop_square_src = img.crop_square_src,
                    crop_wide_src = img.crop_wide_src,
                    crop_enlargement_src = img.crop_enlargement_src,
                    crop_custom_src = img.crop_custom_src
                    )
          try:
            i.save()
          except IntegrityError as e:
            continue
          images.append(i)

        quotes = []
        for quote in story.pull_quotes:
          q = PullQuote(text = quote.text,
                        person = quote.person)
          try:
            q.save()
          except IntegrityError as e:
            continue
          quotes.append(q)

        s = Story(title = story.title,
                  teaser = story.teaser,
                  story_date = story.story_date,
                  byline = story.byline,
                  text = story.text,
                  creation_date = story.creation_date,
                  outlet = "NPR")

        try:
          s.save()
        except IntegrityError as e:
          for i in images:
            i.delete()
          for q in quotes:
            q.delete()
          continue

        for i in images:
          s.images.add(i)

        for q in quotes:
          s.pull_quotes.add(q)

    return success



