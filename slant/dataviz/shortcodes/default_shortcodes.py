#
# default_shortcodes.py
# ~~~~~~~~~~~~~~~~~~~~~
#

from . import base
from . import utils

@utils.register_shortcode('img')
class ImgShortcode(base.Shortcode):
  NUM_REQUIRED_ARGS = 1

  def __init__(self, img_path, static_resource=False): 
    self.img_path = img_path
    self.static_resource = static_resource

  def render(self, context):
    if self.static_resource:
      img_url = utils.render_static_url(self.img_path, context)
    else:
      img_url = self.img_path
    html = [
        '<div class="img-shortcode-wrapper">',
        '<img src={src} width=100% />'.format(src=img_url),
        '</div>'
        ]
    return ''.join(html)
