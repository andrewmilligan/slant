from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from dataviz.models import Story
from dataviz import project_parser
import importlib
import os
import string

class Command(BaseCommand):
  help = 'Reloads local stories and saves them in the db'

  def add_arguments(self, parser):
    parser.add_argument('-d', '--directory',
        default='dataviz.stories.directory',
        type=str)

  def handle(self, *args, **options):

    # slug character helper function
    def isSlugChar(c):
      try:
        return c in string.letters or c in string.whitespace or int(c) in range(10)
      except ValueError:
        pass
      return False

    # try to import the directory module
    dir_mod = options['directory']
    try:
      directory = importlib.import_module(dir_mod)
    except ImportError:
      raise CommandError('Cannot import module "%"' % dir_mod)
    else:

      # parse the stories
      rank = 0
      for proj_file in directory.files:

        # parse the actual story file
        proj_attrs = project_parser.parse_project(proj_file)
        Story_attributes = dir(Story)

        # build the story slug from the title
        slug_chars = ''.join([c for c in proj_attrs['title'] if isSlugChar(c)])
        slug = '-'.join(slug_chars.split()).lower()

        # build params dict for the new story object
        params = {
            'rank': rank,
            'slug': slug,
            }
        for k, v in proj_attrs.iteritems():
          if k in Story_attributes:
            if not callable(getattr(Story, k)) and not k.startswith("__"):
              params[k] = v

        # create (or update) the story object
        p, created = Story.objects.update_or_create(
                    title=params['title'], defaults=params
                    )

        # print result
        if created:
          self.stdout.write("New story '{}' created.".format(p.title))
        else:
          self.stdout.write("Story '{}' updated.".format(p.title))

        rank += 1
