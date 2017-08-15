from django import template

register = template.Library()

from default_shortcodes import *
from user_shortcodes import *
