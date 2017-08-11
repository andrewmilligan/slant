#
#  local_stories_loader.py
#  ~~~~~~~~~~~~~~~~~~~~~~~
#

from . import models 
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import datetime         # for all system time interaction
import json
import markdown
import os

class LocalStoriesLoader:
  #- Requests --------------------------------------------------------------

  def parseMdToStory(self, storyfile):
    story_obj = models.Story()
    lines = []
    with open(storyfile) as f:
      for line in f:
        lines.append(line.rstrip())

    line_num = 0

    # title
    for i in range(len(lines)):
      line = lines[i]
      if "===" not in line:
        story_obj.title += ' '.join(line.split())
      else:
        line_num = i + 1
        break

    # various tags
    for i in range(line_num, len(lines)):
      line = lines[i]
      if line:
        line_split = line.split()

        # @tags
        if line_split[0][0] == "@":
          # author
          if line_split[0] == "@author" and len(line_split) > 1:
            story_obj.byline = ' '.join(line_split[1:])
          # date            
          elif line_split[0] == "@date" and len(line_split) > 1:
            date_list = line_split[1:]
            naive_date_str = ' '.join(date_list[:-1])
            tz = date_list[-1]
            naive_date = datetime.datetime.strptime(
                naive_date_str,
                "%a, %d %b %Y %H:%M:%S")
            new_date_str = "{}-{}-{}T{}:{}:{}{}".format(
                naive_date.year, naive_date.month, naive_date.day,
                naive_date.hour, naive_date.minute, naive_date.second, tz)
            print(new_date_str)
            print(parse_datetime(new_date_str))
            story_obj.story_date = parse_datetime(new_date_str)
          # outlet
          elif line_split[0] == "@outlet" and len(line_split) > 1:
            story_obj.outlet = ' '.join(line_split[1:])
          # local images
          elif line_split[0] == "@localimages" and len(line_split) > 1:
            imgs = ''.join(line_split[1:]).split(',')
            story_obj.images = json.dumps(imgs)
          # Django tags
          elif line_split[0] == "@djangotags" and len(line_split) > 1:
            django_tags = ''.join(line_split[1:]).split(',')

        # [[[ teaser ]]]
        elif line_split[0][0:3] == "[[[":
          if ' '.join(line_split).count("]]]") > 0:
            line_text = ' '.join(line_split).split("[[[", 1)[1].split("]]]", 1)[0]
            story_obj.teaser = markdown.markdown(line_text)
          else:
            teaser = ' '.join(line_split).split("[[[", 1)[1]
            for j in range(i+1, len(lines)):
              teaser_line = lines[j]
              if teaser_line.count("]]]") > 0:
                teaser = ' '.join([teaser, teaser_line.split("]]]", 1)[0]])
                story_obj.teaser = markdown.markdown(teaser)
                line_num = j + 1
                break
              else:
                teaser = ' '.join([teaser, teaser_line])

    # main text
    djtags = ["{{% load {} %}}".format(t) for t in django_tags]
    story_obj.text = os.linesep.join(djtags)
    story_obj.text += markdown.markdown(os.linesep.join(lines[line_num:]))

    return story_obj



  def getLocalStories(self, filename):
    dir_name = os.path.dirname(filename)
    stories = []
    with open(filename) as stories_file:
      stories_json = json.load(stories_file)
    for storyfile in stories_json["stories"]:
      story_path = os.path.join(dir_name, storyfile)
      stories.append(self.parseMdToStory(story_path))
    return stories


  #- End of Requests -------------------------------------------------------
