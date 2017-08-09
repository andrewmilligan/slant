class Story():
  def __init__(self, **kwargs):
    self.title = ''
    self.teaser = ''
    self.story_date = None
    self.byline = ''
    self.text = ''
    self.creation_date = None
    self.images = []
    self.pull_quotes = []

  def __str__(self):
    return self.title


class Image():
  def __init__(self, **kwargs):
    self.src = ''
    self.caption = ''
    self.provider = ''
    self.producer = ''
    self.copyright = ''
    self.crop_standard_src = None
    self.crop_square_src = None
    self.crop_wide_src = None
    self.crop_enlargement_src = None
    self.crop_custom_src = None


class PullQuote():
  def __init__(self, **kwargs):
    self.text = ''
    self.person = ''

  def __unicode__(self):
    return self.text
  
