#
#  message_types.py
#  ~~~~~~~~~~~~~~~~
#

import json
import datetime

#- Master Class ------------------------------------------------------------

class NPRAuthRequest:
  uri = 'authorization/v2/token'
  headers = {}
  params = {
      'grant_type': 'authorization_code',
      'client_id': '',
      'client_secret': '',
      'code': '',
      'redirect_uri': '',
      }
  data = ''
  data_dict = {}

  def __init__(self, client_id='', client_secret=''):
    self.params['client_id'] = client_id
    self.params['client_secret'] = client_secret



class NPRRequest:
  # public
  uri = ''
  headers = {}
  params = {
      'output': 'JSON',
      'fields': 'title,teaser,storyDate,byline,image,textWithHtml,pullQuote',
      'apiKey': '',
      'dateType': 'story',
      'requiredAssets': 'text'
      }
  data = ''
  data_dict = {}

  TOPICS = {
      'business': 1006,
      'business_story_of_the_day': 1095,
      'economy': 1017,
      'education': 1013,
      'environment': 1025,
      'law': 1070,
      'low_wage_america': 1076,
      'media': 1020,
      'national_security': 1122,
      'news': 1001,
      'npr_investigations': 1150,
      'politics': 1014,
      'technology': 1019,
      'usa': 1003,
      'world': 1004,
      'world_story_of_the_day': 1056,
      }

  # private
  __uri_components = []

  def __init__(self, key=None):
    if not key is None:
      self.params['apiKey'] = key

#---------------------------------------------------------------------------

def authRequest(client_id='', client_secret=''):
  req = NPRAuthRequest(client_id, client_secret)
  return req


def newsRequest(key=None):
  req = NPRRequest(key)
  req.params.update({'id': req.TOPICS['news']})
  return req

def politicsRequest(key=None):
  req = NPRRequest(key)
  req.params.update({'id': req.TOPICS['politics']})
  return req

def economyRequest(key=None):
  req = NPRRequest(key)
  req.params.update({'id': req.TOPICS['economy']})
  return req

def businessStoryOfTheDayRequest(key=None):
  req = NPRRequest(key)
  req.params.update({'id': req.TOPICS['business_story_of_the_day']})
  return req

def worldStoryOfTheDayRequest(key=None):
  req = NPRRequest(key)
  req.params.update({'id': req.TOPICS['world_story_of_the_day']})
  return req

def nationalSecurityRequest(key=None):
  req = NPRRequest(key)
  req.params.update({'id': req.TOPICS['national_security']})
  return req

def keywordRequest(keyword, key=None):
  req = NPRRequest(key)
  try:
    req.params.update({'id': req.TOPICS[keyword]})
  except KeyError as e:
    return None
  else:
    return req


