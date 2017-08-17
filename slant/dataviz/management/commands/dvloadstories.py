from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from dataviz.models import Story
from dataviz.local_stories_loader import LocalStoriesLoader
import importlib
import os

class Command(BaseCommand):
  help = 'Reloads local stories and saves them in the db'

  def add_arguments(self, parser):
    parser.add_argument('-d', '--directory',
        default='dataviz.stories.directory',
        type=str)

  def handle(self, *args, **options):
    dir_mod = options['directory']
    try:
      directory = importlib.import_module(dir_mod)
    except ImportError:
      raise CommandError('Cannot import module "%"' % dir_mod)
    else:
      bot = LocalStoriesLoader()
      stories = bot.getLocalStories(directory.files)

      if stories:
        for s in stories:
          try:
            s.save()
          except IntegrityError as e:
            s_orig = Story.objects.get(title=s.title)
            s_orig.title = s.title
            s_orig.teaser = s.teaser
            s_orig.byline = s.byline
            s_orig.text = s.text
            s_orig.creation_date = s.creation_date
            s_orig.story_date = s.story_date
            s_orig.outlet = s.outlet
            s_orig.images = s.images
            s_orig.rank = s.rank
            s_orig.save()
