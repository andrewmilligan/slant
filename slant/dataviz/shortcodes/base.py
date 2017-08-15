#
# shortcode_base.py
# ~~~~~~~~~~~~~~~~~
#
# This file defines the base Shortcode class. All shortcodes should subclass
# this base class to ensure that they work properly as Django-recognized
# template tags.
#

from django import template

class Shortcode(template.Node):
  # data members (should be treated as const); can be overwritten by subclasses
  NUM_REQUIRED_ARGS = 1

  @classmethod
  def handle_token(cls, parser, token):
    tokens = token.split_contents()
    # first token is tag name, so make sure we have enough args
    if len(tokens) <= cls.NUM_REQUIRED_ARGS:
      raise template.TemplateSyntaxError(
          "{} tag requires at least {} arguments".format(
            token.contents.split()[0], cls.NUM_REQUIRED_ARGS))

    args = []
    kwargs = {}
    arg_tokens = tokens[1:] # ignore tag name

    if arg_tokens:
      for token in arg_tokens:
        match = template.base.kwarg_re.match(token)
        if not match:
          raise template.TemplateSynatxError(
              "Malformed argument(s) to {} tag: {}".format(
                token.contents.split()[0], token))
        name, value = match.groups()
        if name:
          kwargs[name] = parser.compile_filter(value)
        else:
          args.append(parser.compile_filter(value))

    return cls(*args, **kwargs)

  def resolve_safe(self, f, context):
    res = f
    try:
      res = f.resolve(context)
    except AttributeError:
      pass
    return res

  def render(self, context):
    return ''

