#
#  twitter_requests.py
#  ~~~~~~~~~~~~~~~~~~~
#

import json
import datetime
import base64
from django.utils.http import urlencode

#- Master Class ------------------------------------------------------------

class TwitterRequest:
  # public
  uri = ''
  headers = {
      'Authorization': 'Bearer ',
      }
  params = {}
  data = ''
  data_dict = {}

  def __init__(self, key=None):
    if not key is None:
      self.headers['Authorization'] = ' '.join(["Bearer", key])



class TwitterAuthRequest:
  uri = 'oauth2/token'
  headers = {
      'Authorization': '',
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
      }
  params = {
      'grant_type': 'client_credentials'
      }
  data = ''
  data_dict = {}

  def __init__(self, client_id, client_secret):
    key_str = ':'.join([client_id, client_secret])
    self.headers['Authorization'] = ' '.join(["Basic",
      base64.b64encode(key_str)])



class UserTimelineRequest(TwitterRequest):
  uri = '1.1/statuses/user_timeline.json'
  params = {
      'screen_name': '',
      'count': 10,
      }

  def __init__(self, key, user='', count=10):
    self.headers['Authorization'] = ' '.join(["Bearer", key])
    self.params['screen_name'] = user
    self.params['count'] = count



class SearchRequest(TwitterRequest):
  uri = '1.1/search/tweets.json'
  params = {
      'q': '',
      'result_type': 'recent',
      }

  def __init__(self, key, q='', response_type="recent"):
    self.headers['Authorization'] = ' '.join(["Bearer", key])
    self.params['q'] = q
    self.params['response_type'] = response_type


class OEmbedRequest:
  uri = 'oembed'
  headers = {}
  params = {
      'url': '',
      }
  data = ''
  data_dict = {}

  def __init__(self, url):
    self.params['url'] = urlencode(url)


#---------------------------------------------------------------------------
