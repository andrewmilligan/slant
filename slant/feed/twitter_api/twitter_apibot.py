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
      print(response.request.url)
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
    if not tweets:
      print("No tweets found.")
    for t in tweets:
      tweet_obj = models.Tweet()
      try:
        tweet_obj.screen_name = t['user']['screen_name']
        tweet_obj.id = t['id']
        tweet_obj.html = self.embed(tweet_obj)
      except KeyError as e:
        print("Tweet busted from: {}".format(e))
        continue
        
      tweet_objects.append(tweet_obj)

    return tweet_objects

  def requestJson(self, msg, base_uri=None):
    rsp = self.GET(msg, base_uri)
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

  def embed(self, tweet):
    msg = messages.OEmbedRequest(tweet.screen_name, tweet.id)
    rsp_json = self.requestJson(msg, "https://publish.twitter.com")
    return rsp_json['html']

  #- End of Requests -------------------------------------------------------
