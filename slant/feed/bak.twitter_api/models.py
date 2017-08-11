class Tweet():
  def __init__(self, **kwargs):
    self.user = None
    self.text = ''
    self.created_at = ''
    self.media = []
    self.uris = []

  def __str__(self):
    return self.text

class Media():
  def __init__(self):
    self.uri = ''
    self.expanded_uri = ''
    self.display_uri = ''

  def __str__(self):
    return self.display_uri

  def setFromJSON(self, js):
    self.uri = js['url']
    self.expanded_uri = js['expanded_url']
    self.display_uri = js['display_url']

class URI():
  def __init__(self):
    self.uri = ''
    self.expanded_uri = ''
    self.display_uri = ''

  def __str__(self):
    return self.display_uri

  def setFromJSON(self, js):
    self.uri = js['url']
    self.expanded_uri = js['expanded_url']
    self.display_uri = js['display_url']

class TwitterUser():
  def __init__(self):
    self.name = ''
    self.screen_name = ''
    self.profile_image_url_https = ''

  def __str__(self):
    return self.name

  def setFromJSON(self, js):
    self.name = js['name']
    self.screen_name = js['screen_name']
    self.profile_image_url_https = js['profile_image_url_https']


