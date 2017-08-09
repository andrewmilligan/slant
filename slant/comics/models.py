from __future__ import unicode_literals

from django.db import models

import xkcd_api

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
    comics = bot.getCurrentComic()
    success = False
    if comics:
      success = True

      for old_comic in cls.objects.all():
        old_comic.delete()

      for comic in comics:
        c = cls(title = comic.title,
                image_src = comic.image_src,
                hover_text = comic.hover_text,
                num = comic.num,
                outlet = comic.outlet)
        c.save()

    return success




