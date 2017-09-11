from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from portfolio.models import Project
from portfolio import project_parser
import importlib
import os
import string

class Command(BaseCommand):
  help = 'Reloads local projects and saves them in the db'

  def add_arguments(self, parser):
    parser.add_argument('-d', '--directory',
        default='portfolio.projects.directory',
        type=str)

  def handle(self, *args, **options):

    # slug
    def isSlugChar(c):
      try:
        return c in string.letters or c in string.whitespace or int(c) in range(10)
      except ValueError:
        pass
      return False

    dir_mod = options['directory']
    try:
      directory = importlib.import_module(dir_mod)
    except ImportError:
      raise CommandError('Cannot import module "%"' % dir_mod)
    else:
      rank = 0
      for proj_file in directory.files:
        proj_attrs = project_parser.parse_project(proj_file)
        Project_attributes = dir(Project)
        slug_chars = ''.join([c for c in proj_attrs['title'] if isSlugChar(c)])
        slug = '-'.join(slug_chars.split()).lower()
        params = {
            'rank': rank,
            'slug': slug,
            }
        for k, v in proj_attrs.iteritems():
          if k in Project_attributes:
            if not callable(getattr(Project, k)) and not k.startswith("__"):
              params[k] = v
        p, created = Project.objects.update_or_create(
                    title=params['title'], defaults=params
                    )
        if created:
          self.stdout.write("New project '{}' created.".format(p.title))
        else:
          self.stdout.write("Project '{}' updated.".format(p.title))
        rank += 1
