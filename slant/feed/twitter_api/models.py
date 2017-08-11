class Tweet():
  def __init__(self, **kwargs):
    self.screen_name = ''
    self.id = None
    self.html = ''

  def __str__(self):
    return "{} {}".format(self.screen_name, self.id)
