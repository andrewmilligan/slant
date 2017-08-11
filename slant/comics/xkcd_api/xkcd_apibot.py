#
#  xkcd_apibot.py
#  ~~~~~~~~~~~~~~
#

# Python Imports
import ssl        # for HTTPS
import requests   # Python module for HTTP requests

# Stratosphere Imports
from . import models 
import messages         # message objects for API message types
import api_exceptions   # custom exception classes
import json

class XkcdAPIBot:
  #- Data Members ----------------------------------------------------------
  # base URI
  # this can be overwritten in the API Bot config file
  base_uri = 'http://xkcd.com'

  # timeout for HTTP requests
  timeout = 3
  off_ping_rt = 45
  on_ping_rt = 20
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
  #  @param msg a GatewayToServer message object
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

  #- end of HTTP request abstractions --------------------------------------



  #- Requests --------------------------------------------------------------

  def parseJsonToComicList(self, json_obj):
    comic_list = []
    new_comic = models.Comic()
    new_comic.title = json_obj['title']
    new_comic.image_src = json_obj['img']
    new_comic.num = int(json_obj['num'])
    new_comic.hover_text = json_obj['alt']
    new_comic.outlet = "xkcd"
    comic_list.append(new_comic)
    return comic_list

  def requestJson(self, msg):
    rsp = self.GET(msg)
    try:
      rsp_json = rsp.json()
    except ValueError as e:
      raise api_exceptions.APIValueError(e)
    return rsp_json

  def getCurrentComic(self):
    msg = messages.currentComicRequest()
    return self.parseJsonToComicList(self.requestJson(msg))

  def getComicNumStories(self, num):
    msg = messages.comicNumRequest(num)
    return self.parseJsonToComicList(self.requestJson(msg))

  #- End of Requests -------------------------------------------------------
