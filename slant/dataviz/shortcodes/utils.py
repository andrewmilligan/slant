#
# utils.py
# ~~~~~~~~
#
# This file defines several helper functions for the shortcodes system,
# including functions for registration of shortcodes in the system and
# reversing URLs. These try to avoid repetetive effort on the part of the user
# in defining new shortcodes.
#

from django import template
from django.urls import reverse, NoReverseMatch
from django.templatetags.static import static

from .shortcodes import register


'''
Shortcode registration.
This function can be used either as a free function or as a class decorator for
subclasses of the Shortcode base class.
'''

def register_shortcode_class(cls):
  name = cls.__name__.lower()
  register.tag(name=name, compile_function=cls.handle_token)

def register_shortcode(name=None, cls=None):
  if name is None and cls is None:
    # @register_shortcode()
		return register_shortcode_class
  elif name is not None and cls is None:
    # @register_shortcode
    if callable(name):
      cls = name
      return register_shortcode_class(cls)
    else:
      # @register_shortcode('somename') or @register_shortcode(name='somename')
      def dec(cls):
        return register_shortcode(name, cls)
      return dec
  elif name is not None and cls is not None:
    # register_shortcode('somename', somecls)
    register.tag(name=name, compile_function=cls.handle_token)
    return cls
  else:
		raise ValueError(
				"Unsupported arguments to register_shortcode: (%r, %r)" %
				(name, compile_function),
		)


'''
Filter to help make a separated list out of a string.
'''
@register.filter
def seplist(s, sep=' '):
  return s.split(sep)


'''
Django URL lookup.
This code was adapted from the source code of the render function for the
Django built-in URL template tag.
'''
def as_url(url_str, context):
  try:
    current_app = context.request.current_app
  except AttributeError:
    try:
      current_app = context.request.resolver_match.namespace
    except AttributeError:
      current_app = None
  # Try to look up the URL. If it fails, raise NoReverseMatch
  url = ''
  try:
    url = reverse(view_name, args=args, kwargs=kwargs, current_app=current_app)
  except NoReverseMatch:
    raise


'''
Django static resource lookup.
'''
def render_static_url(url_str, context):
  return static(url_str)
