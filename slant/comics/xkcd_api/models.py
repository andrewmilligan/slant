class Comic():
  def __init__(self, **kwargs):
    self.title = ''
    self.image_src = ''
    self.hover_text = ''
    self.outlet = ''
    self.num = 0

  def __unicode__(self):
    return self.title
  
