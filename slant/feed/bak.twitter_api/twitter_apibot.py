#
#  twitter_apibot.py
#  ~~~~~~~~~~~~~~~~~
#

# Python Imports
import ssl        # for HTTPS
import requests   # Python module for HTTP requests

# Stratosphere Imports
import models 
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.encoding import smart_str
import datetime         # for all system time interaction
import messages         # message objects for API message types
import api_exceptions   # custom exception classes
import json
import twitter_auth

class TwitterAPIBot:
  #- Data Members ----------------------------------------------------------
  # used for configuration
  initialized = False
  file_path = ''
  repo_root = ''
  base_uri = ''
  parser = ''

  # base URI
  # this can be overwritten in the API Bot config file
  base_uri = 'https://api.twitter.com'

  # timeout for HTTP requests
  timeout = 3
  off_ping_rt = 45
  on_ping_rt = 20

  #api_key = 'MDI5NzM2OTIzMDE0ODQxNjE2OTk5OTZkYw000'
  auth = twitter_auth.TwitterAPIAuth()
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
  def GET(self, msg, base_uri=None):
    # Send Request.
    #
    # Else, extract necessary information from the message object
    # to formulate and send the request.
    # If any of this fails, decide that we're offline and raise
    # an exception.
    # If it succeeds, we are online. Return the response.
    #
    if base_uri is None:
      base_uri = self.base_uri
    try:
      uri = '/'.join([base_uri, msg.uri])
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
  def POST(self, msg, base_uri=None):
    # Send Request.
    #
    # Else, extract necessary information from the message object
    # to formulate and send the request.
    # If any of this fails, decide that we're offline, cache the
    # message, and raise an exception.
    # If it succeeds, we are online. Return the response.
    #
    if base_uri is None:
      base_uri = self.base_uri
    try:
      uri = '/'.join([base_uri, msg.uri])
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

  def parseJsonToTweetList(self, json_obj):
    tweets = json_obj['statuses']
    tweet_objects = []
    for s in tweets:
      tweet_obj = models.Tweet()
      try:
        tweet_obj.user = models.TwitterUser()
        tweet_obj.user.setFromJSON(s['user'])

        tweet_obj.text = smart_str(s['text'])

        date_list = s['created_at'].split()
        naive_date_str = ' '.join(date_list[:-2] + [date_list[-1]])
        tz = "Z" 
        naive_date = datetime.datetime.strptime(
            naive_date_str,
            "%a %b %d %H:%M:%S %Y")
        new_date_str = "{}-{}-{}T{}:{}:{}{}".format(
            naive_date.year, naive_date.month, naive_date.day,
            naive_date.hour, naive_date.minute, naive_date.second, tz)
        tweet_obj.created_at = parse_datetime(new_date_str)

        try:
          for u in s['entities']['urls']:
            new_uri = models.URI()
            new_uri.setFromJSON(u)
            tweet_obj.uris.append(new_uri)
        except KeyError as e:
          pass

        try:
          for m in s['entities']['media']:
            new_media = models.URI()
            new_media.setFromJSON(m)
            tweet_obj.uris.append(new_media)
        except KeyError as e:
          pass

      except KeyError as e:
        continue
        
      tweet_objects.append(tweet_obj)

    return tweet_objects

  def requestJson(self, msg):
    rsp = self.GET(msg)
    try:
      rsp_json = rsp.json()
    except ValueError as e:
      raise api_exceptions.APIValueError(e)
    return rsp_json

  def getSearch(self, q, result_type='recent'):
    msg = messages.SearchRequest(self.apiKey(), q, result_type)
    return self.parseJsonToTweetList(self.requestJson(msg))

  # Get Auth Token
  def getAuthToken(self):
    msg = messages.TwitterAuthRequest(self.auth.application_id,
        self.auth.application_secret)

    rsp = self.POST(msg)
    try:
      rsp_json = rsp.json()
    except ValueError as e:
      raise api_exceptions.APIValueError(e)

    try:
      if rsp_json['token_type'] != 'bearer':
        raise api_exceptions.AuthError(Exception("auth token of non-bearer type"))
      api_key = rsp_json['access_token']
    except KeyError as e:
      raise api_exceptions.AuthError(e)
    else:
      return api_key

  def apiKey(self):
    return self.auth.api_key

  def authenticate(self):
    self.auth.api_key = self.getAuthToken()


  #- End of Requests -------------------------------------------------------
