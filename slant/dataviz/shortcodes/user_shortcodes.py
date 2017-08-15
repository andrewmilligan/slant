#
# user_shortcodes.py
# ~~~~~~~~~~~~~~~~~~
#

'''
Define shortcodes as Python classes that inherit from the class
`hoodwink.shortcodes.base.Shortcode`. The static data member
`num_required_args` should be overwritten for clarity, though the default is
one. This argument *must* be treated as constant and never changed.

The class constructor (__init__) must take the argument `self` (per Python),
and can take any additional arguments you like, either positional (e.g.,
`__init__(self, foo)`) or keyword (e.g., `__init__(self, foo=bar)`). You should
make sure that the number of arguments to `__init__` is at least
`NUM_REQUIRED_ARGS`, though there can be more.

Additionally, the class must define a `render` member function. This function
only takes two arguments: `self` (as required for member functions), and a
context variable. The context is used to resolve the actual values of variables
in a thread-safe manner. The render function is responsible for returning the
actual HTML you want to be in the page in place of the shortcode as a string.
'''

from . import base
from . import utils

# define your shortcode classes here

from django import template
import markdown
import os

@utils.register_shortcode('graph')
class GraphShortcode(base.Shortcode):
  NUM_REQUIRED_ARGS = 1

  def __init__(self, img_path, title=None, subtitle=None, footnote=None, static_resource=True): 
    self.img_path = img_path
    self.title = title
    self.subtitle = subtitle
    self.footnote = footnote
    self.static_resource = static_resource

  def render(self, context):
    # img url
    img_path = self.resolve_safe(self.img_path, context)
    img_url = utils.render_static_url(img_path, context)

    title = self.resolve_safe(self.title, context)
    subtitle = self.resolve_safe(self.subtitle, context)
    footnote = self.resolve_safe(self.footnote, context)
    static_resource = self.resolve_safe(self.static_resource, context)

    title_html = ''
    if not title is None:
      title_html = '<div class="title">{}</div>'.format(title)

    subtitle_html = ''
    if not subtitle is None:
      subtitle = markdown.markdown(subtitle)
      subtitle_html = '<div class="subtitle">{}</div>'.format(subtitle)

    body_html = '<img src={src} width=100% />'.format(src=img_url)

    footnote_html = ''
    if not footnote is None:
      footnote = markdown.markdown(footnote)
      footnote_html = '<div class="footnote">{}</div>'.format(footnote)

    html = [
        '<div class="graph-shortcode-wrapper">',
        title_html,
        subtitle_html,
        body_html,
        footnote_html,
        '</div>'
        ]
    return os.linesep.join(html)




@utils.register_shortcode('graphanim')
class GraphAnimShortcode(base.Shortcode):
  NUM_REQUIRED_ARGS = 2

  def __init__(self, img_paths, anim_id, title=None, subtitle=None, footnote=None): 
    self.img_paths = img_paths
    self.anim_id = anim_id
    self.title = title
    self.subtitle = subtitle
    self.footnote = footnote

  def render(self, context):
    # img url
    img_urls = self.resolve_safe(self.img_paths, context)

    title = self.resolve_safe(self.title, context)
    subtitle = self.resolve_safe(self.subtitle, context)
    footnote = self.resolve_safe(self.footnote, context)
    anim_id = self.resolve_safe(self.anim_id, context)

    title_html = ''
    if not title is None:
      title_html = '<div class="title">{}</div>'.format(title)

    subtitle_html = ''
    if not subtitle is None:
      subtitle = markdown.markdown(subtitle)
      subtitle_html = '<div class="subtitle">{}</div>'.format(subtitle)

    body_html = []
    for img_url in img_urls:
      img = utils.render_static_url(img_url, context)
      body_html.append('<img class="slide-{aid}" src={src} width=100% />'.format(
        src=img, aid=anim_id))
    body_html = os.linesep.join(body_html)

    footnote_html = ''
    if not footnote is None:
      footnote = markdown.markdown(footnote)
      footnote_html = '<div class="footnote">{}</div>'.format(footnote)

    script_lines = [ '<script>',
        'var slideIndex = 0;',
        'carousel();',
        'function carousel() {',
        '  var i;',
        '  var x = document.getElementsByClassName("slide-' + str(anim_id) + '");',
        '  for (i = 0; i < x.length; i++) {',
        '    x[i].style.display = "none";',
        '  }',
        '  slideIndex++;',
        '  if (slideIndex > x.length) {slideIndex = 1}',
        '  x[slideIndex-1].style.display = "block";',
        '  setTimeout(carousel, 500); // Change image every 0.5 second',
        '}',
        '</script>'
        ]
    script = os.linesep.join(script_lines)

    html = [
        '<div class="graph-shortcode-wrapper">',
        title_html,
        subtitle_html,
        body_html,
        footnote_html,
        '</div>',
        script
        ]
    return os.linesep.join(html)
