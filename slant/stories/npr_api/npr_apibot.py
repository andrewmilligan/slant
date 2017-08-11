#
#  npr_apibot.py
#  ~~~~~~~~~~~~~
#

# Python Imports
import ssl        # for HTTPS
import requests   # Python module for HTTP requests

# Stratosphere Imports
import models 
from django.utils import timezone
from django.utils.dateparse import parse_datetime
import datetime         # for all system time interaction
import messages         # message objects for API message types
import api_exceptions   # custom exception classes
import json
import npr_auth

class NPRAPIBot:
  #- Data Members ----------------------------------------------------------
  # used for configuration
  initialized = False
  file_path = ''
  repo_root = ''
  base_uri = ''
  parser = ''

  # base URI
  # this can be overwritten in the API Bot config file
  base_uri = 'https://api.npr.org'
  api_version = 'Calcium'

  # timeout for HTTP requests
  timeout = 3
  off_ping_rt = 45
  on_ping_rt = 20

  #api_key = 'MDI5NzM2OTIzMDE0ODQxNjE2OTk5OTZkYw000'
  auth = npr_auth.NPRAPIAuth()
  #-------------------------------------------------------------------------

  #- Initialization --------------------------------------------------------

  def __init__(self, logger=None, cache=None):
    # Strip trailing slash from base_uri if necessary.
    #
    # split URI on slashes; if the last element is empty, there was
    # a trailing slash, so remove the last (empty) element from the
    # list and recombine the rest, leaving off the trailing slash.
    #
    uri_components = self.base_uri.split('/')
    if len(uri_components) > 0 and uri_components[-1] == '':
      uri_components.pop()
      self.base_uri = '/'.join(uri_components)

  #-------------------------------------------------------------------------


  #- HTTP Request Abstractions ---------------------------------------------

  ## HTTP Get Method.
  #
  #  This abstracts an HTTP Get request using the Requests module.
  #  It takes an API GatewayToServer message object and uses it to
  #  formulate and send the request.
  #
  #  This is meant to be a helper function for the API abstractions, and
  #  not an outward-facing function. However, it can be used to send
  #  user-designed message objects to the API.
  #
  def GET(self, msg):
    # Send Request.
    #
    # Else, extract necessary information from the message object
    # to formulate and send the request.
    # If any of this fails, decide that we're offline and raise
    # an exception.
    # If it succeeds, we are online. Return the response.
    #
    try:
      uri = '/'.join([self.base_uri, msg.uri])
      response = requests.get(uri,
                              headers=msg.headers,
                              params=msg.params,
                              data=msg.data,
                              timeout=self.timeout,
                              verify=True)
    except requests.exceptions.RequestException as e:
      raise api_exceptions.RequestError(e, uri)
    else:
      return response

  ## HTTP Post Method.
  #
  #  This abstracts an HTTP Post request using the Requests module.  It takes a
  #  message object and uses it to formulate and send the request.
  #
  #  This is meant to be a helper function for the API abstractions, and not an
  #  outward-facing function. However, it can be used to send user-designed
  #  message objects to the API.
  #
  def POST(self, msg):
    # Send Request.
    #
    # Else, extract necessary information from the message object
    # to formulate and send the request.
    # If any of this fails, decide that we're offline, cache the
    # message, and raise an exception.
    # If it succeeds, we are online. Return the response.
    #
    try:
      uri = '/'.join([self.base_uri, msg.uri])
      response = requests.post(uri,
                               headers=msg.headers,
                               params=msg.params,
                               data=msg.data,
                               timeout=self.timeout,
                               verify=True)
    except requests.exceptions.RequestException as e:
      raise api_exceptions.RequestError(e, uri)
    else:
      return response

  #- end of HTTP request abstractions --------------------------------------



  #- Requests --------------------------------------------------------------

  def parseJsonToStoryList(self, json_obj):
    stories = json_obj['list']['story']
    story_objects = []
    for s in stories:
      story_obj = models.Story()
      try:
        title = s['title']['$text']
        story_obj.title = u"{}".format(title)
        story_obj.teaser = s['teaser']['$text']
        story_obj.creation_date = timezone.now()

        date_list = s['storyDate']['$text'].split()
        naive_date_str = ' '.join(date_list[:-1])
        tz = date_list[-1]
        naive_date = datetime.datetime.strptime(
            naive_date_str,
            "%a, %d %b %Y %H:%M:%S")
        new_date_str = "{}-{}-{}T{}:{}:{}{}".format(
            naive_date.year, naive_date.month, naive_date.day,
            naive_date.hour, naive_date.minute, naive_date.second, tz)
        story_obj.story_date = parse_datetime(new_date_str)

        try:
          story_obj.outlet = s['outlet']
        except KeyError:
          story_obj.outlet = "NPR"

        s_paragraphs = []
        for paragraph in s['textWithHtml']['paragraph']:
          s_paragraphs.append(u"<p>{}</p>".format(paragraph['$text']))
        story_obj.text = ' '.join(s_paragraphs)

      except KeyError as e:
        continue

      try:
        story_obj.byline = json.dumps(s['byline'])
      except KeyError as e:
        story_obj.byline = None

      try:
        for img in s['image']:
          new_img = models.Image()
          try:
            new_img.src = img['src']
            for crop in img['crop']:
              if crop['type'] == 'standard':
                new_img.crop_standard_src = crop['src']
              elif crop['type'] == 'square':
                new_img.crop_square_src = crop['src']
              elif crop['type'] == 'wide':
                new_img.crop_wide_src = crop['src']
              elif crop['type'] == 'enlargement':
                new_img.crop_enlargement_src = crop['src']
              elif crop['type'] == 'custom':
                new_img.crop_custom_src = crop['src']
            try:
              new_img.caption = img['caption']['$text']
              new_img.provider = img['provider']['$text']
              new_img.producer = img['producer']['$text']
              new_img.copyright = img['copyright']
            except KeyError as e:
              pass
          except KeyError as e:
            continue
          else:
            story_obj.images.append(new_img)
      except KeyError as e:
        story_obj.images = []

      try:
        for quote in s['pullQuote']:
          new_quote = models.PullQuote()
          try:
            new_quote.text = quote['text']['$text']
            new_quote.person = quote['person']['$text']
          except KeyError as e:
            continue
          else:
            story_obj.pull_quotes.append(new_quote)
      except KeyError as e:
        story_obj.pull_quotes = []
        
      story_objects.append(story_obj)

    return story_objects

  def requestJson(self, msg):
    rsp = self.GET(msg)
    print(rsp.text)
    try:
      rsp_json = rsp.json()
    except ValueError as e:
      raise api_exceptions.APIValueError(e)
    return rsp_json

  def getPoliticsStories(self):
    self.authorize()
    msg = messages.politicsRequest(self.apiKey())
    return self.parseJsonToStoryList(self.requestJson(msg))

  def getNewsStories(self):
    self.authorize()
    msg = messages.newsRequest(self.apiKey())
    return self.parseJsonToStoryList(self.requestJson(msg))

  # Get Auth Token
  def getAuthToken(self):
    msg = messages.authRequest(self.auth.application_id,
        self.auth.application_secret)

    rsp = self.POST(msg)
    try:
      rsp_json = rsp.json()
    except ValueError as e:
      raise api_exceptions.APIValueError(e)

    print(rsp_json)
    try:
      api_key = rsp_json['access_token']
    except KeyError as e:
      raise api_exceptions.AuthError(e)
    else:
      return api_key

  def apiKey(self):
    return self.auth.api_key

  def authorize(self):
    self.auth.api_key = self.getAuthToken()


  #- End of Requests -------------------------------------------------------
