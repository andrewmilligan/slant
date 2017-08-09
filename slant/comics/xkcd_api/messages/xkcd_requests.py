#
#  message_types.py
#  ~~~~~~~~~~~~~~~~
#

import json
import datetime

#- Master Class ------------------------------------------------------------

class XkcdRequest:
  # public
  uri = 'info.0.json'
  headers = {}
  params = {}
  data = ''
  data_dict = {}

  # private
  __uri_components = []

  def __init__(self):
    pass

#---------------------------------------------------------------------------

def currentComicRequest():
  req = XkcdRequest()
  return req

def comicNumRequest(num):
  req = XkcdRequest()
  req.uri = '/'.join([ str(num), 'info.0.json' ])
  return req
