from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
  slug = models.CharField(max_length=200, default='')
  title = models.CharField(max_length=200, default='', unique=True)
  teaser = models.TextField(default='')
  text = models.TextField(default='')
  image = models.TextField(default='')
  rank = models.IntegerField(null=True)

  def __unicode__(self):
    return self.title.encode('ascii', 'ignore')
