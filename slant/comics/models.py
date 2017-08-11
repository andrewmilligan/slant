from __future__ import unicode_literals

from django.db import models

import xkcd_api
import random

# Create your models here.

class Comic(models.Model):
  title = models.CharField(max_length=200, default='')
  image_src = models.URLField(default='')
  hover_text = models.TextField(null=True)
  outlet = models.CharField(max_length=200, default='', null=True)
  num = models.IntegerField(null=True)

  @classmethod
  def check_for_new(cls):
    bot = xkcd_api.XkcdAPIBot()
    comic = bot.getCurrentComic()
    success = False
    if not comic is None:
      success = True
      cls.objects.all().delete()
      c = cls(title = comic.title,
              image_src = comic.image_src,
              hover_text = comic.hover_text,
              num = comic.num,
              outlet = comic.outlet)
      c.save()
      return c
    return None

  @classmethod
  def get_random(cls):
    bot = xkcd_api.XkcdAPIBot()
    # get current comic to find max num. Min num is 1
    newest_comic = bot.getCurrentComic()
    if not newest_comic is None:
      i = random.randrange(1, newest_comic.num + 1)
      comic = bot.getComicNum(i)
      if not comic is None:
        cls.objects.all().delete()
        c = cls(title = comic.title,
                image_src = comic.image_src,
                hover_text = comic.hover_text,
                num = comic.num,
                outlet = comic.outlet)
        c.save()
        return c
    return None




