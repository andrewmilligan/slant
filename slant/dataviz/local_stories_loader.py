#
#  local_stories_loader.py
#  ~~~~~~~~~~~~~~~~~~~~~~~
#

import models 
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import datetime         # for all system time interaction
import json
import markdown
import os

class LocalStoriesLoader:
  #- Requests --------------------------------------------------------------

  def parseMdToStory(self, storyfile):
    # TODO: handle bad inputs gracefully.

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
            if line_split[1] == "today":
              story_obj.story_date = timezone.now()
            else:
              date_list = line_split[1:]
              naive_date_str = ' '.join(date_list[:-1])
              tz = date_list[-1]
              naive_date = datetime.datetime.strptime(
                  naive_date_str,
                  "%a, %d %b %Y %H:%M:%S")
              new_date_str = "{}-{}-{}T{}:{}:{}{}".format(
                  naive_date.year, naive_date.month, naive_date.day,
                  naive_date.hour, naive_date.minute, naive_date.second, tz)
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
            #story_obj.teaser = markdown.markdown(line_text)
            story_obj.teaser = line_text
          else:
            teaser = ' '.join(line_split).split("[[[", 1)[1]
            for j in range(i+1, len(lines)):
              teaser_line = lines[j]
              if teaser_line.count("]]]") > 0:
                teaser = ' '.join([teaser, teaser_line.split("]]]", 1)[0]])
                #story_obj.teaser = markdown.markdown(teaser)
                story_obj.teaser = teaser
                line_num = j + 1
                break
              else:
                teaser = ' '.join([teaser, teaser_line])

    # main text
    djtags = ["{{% load {} %}}".format(t) for t in django_tags]
    story_obj.text = os.linesep.join(djtags)
    #story_obj.text += markdown.markdown(os.linesep.join(lines[line_num:]))
    story_obj.text += os.linesep.join(lines[line_num:])

    return story_obj



  def getLocalStories(self, files):
    stories = []
    for story_path in files:
      stories.append(self.parseMdToStory(story_path))
    return stories


  #- End of Requests -------------------------------------------------------
