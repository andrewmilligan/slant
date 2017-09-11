import re
import shlex
import os
import markdown

### Regular Expressions #######################################################

# Tile: anything before at least three equal signs at the start of a line
title_re = re.compile(r'^(?P<title>.*?)\s*\n={3}=*\s*?$',
    re.DOTALL | re.MULTILINE)

# Teaser: block of text between `[[[` and `]]]`
teaser_re = re.compile(r'\[\[\[\s*(?P<teaser>.*?)\s*\]\]\]\s*?$',
    re.DOTALL | re.MULTILINE)

# Tag: `@tags` set meta-data about the story
def tag_re(tagname):
  # start of line
  # optional space
  # "@tagname"
  # at least one space (if there are ags)
  # args
  # trailing white space, end of line
  tag_pattern = r'^\s*?@{}(?:\s+(?P<args>.*?))?\s*?$'.format(tagname)
  return re.compile(tag_pattern, re.MULTILINE)

# Key-word Arguments: utility for parsing out arguments in blocks
def parse_kwargs(kwarg_str):
  kwarg_p = r'^\s*(?P<kw>\S*?)\s*=\s*(?P<quote>[",\'])(?P<arg>.*?)(?<!\\)(?P=quote)\s*$'
  kwarg_re = re.compile(kwarg_p, re.DOTALL | re.MULTILINE)
  kwargs = {}
  for kv in re.finditer(kwarg_re, kwarg_str):
    kv_dict = kv.groupdict()
    kwargs.update({kv_dict['kw']: kv_dict['arg']})
  return kwargs

# Blocks: inside curly braces with a `@name` and keyword arguments
def block_re(blockname):
  bp = r'^\s*?{{\s*?@{}\s*?(?:\s+(?P<args>.*?))?\s*}}\s*?$'.format(blockname)
  return re.compile(bp, re.DOTALL | re.MULTILINE)

###############################################################################



### Parsers ###################################################################

### Tag Parsers: these determine how a tag's arguments will be interpreted to
#                form the "value" of the meta-data specified by the tag

# Parse everything on the line with the tag as the value
def parse_tag_wholeline(args):
  return str(args)

# Parse the rest of the line as a comma-separated list of values
def parse_tag_csv(args):
  return [a.strip() for a in args.split(',')]


### Block Parsers: these determine what HTML will replace the block in the text
#                  of the story

# Graph Block
def parse_block_graph(img_path, title=None, subtitle=None, footnote=None):
  title_html = ''
  if not title is None:
    title_html = '<div class="title">{}</div>'.format(title)

  subtitle_html = ''
  if not subtitle is None:
    subtitle = markdown.markdown(subtitle)
    subtitle_html = '<div class="subtitle">{}</div>'.format(subtitle)

  body_html = '<img src={src} width=100% />'.format(src=img_path)

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
      '</div>',
      ]
  return os.linesep.join(html)

###############################################################################


registered_tags = {
    "author": parse_tag_wholeline,
    "date": parse_tag_wholeline,
    "outlet": parse_tag_wholeline,
    "djangotags": parse_tag_csv,
    "image": parse_tag_wholeline,
    }

registered_blocks = {
    "graph": parse_block_graph,
    }


def parse_blocks(text):
  for block, block_parser in registered_blocks.iteritems():
    b_re = block_re(block)
    b_match = re.search(b_re, text)
    if b_match:
      kwargs = {}
      if "args" in b_match.groupdict():
        kwargs = parse_kwargs(b_match.group('args'))
      block_html = block_parser(**kwargs)
      text = os.linesep.join([text[:b_match.start()],
        block_html,
        text[b_match.end():]])
  return text


def parse_project(fname):
  with open(fname) as f:
    ftext = f.read()

  title = ''
  title_match = re.search(title_re, ftext)
  if title_match:
    title = title_match.group('title')
    ftext = ' '.join([ftext[:title_match.start()],
      ftext[title_match.end():]])

  teaser = ''
  teaser_match = re.search(teaser_re, ftext)
  if teaser_match:
    teaser = teaser_match.group('teaser')
    ftext = ' '.join([ftext[:teaser_match.start()],
      ftext[teaser_match.end():]])

  attributes = {
      'title': title,
      'teaser': teaser,
      }
  for tag, tag_parser in registered_tags.iteritems():
    t_re = tag_re(tag)
    t_match = re.search(t_re, ftext)
    if t_match:
      args = ''
      if "args" in t_match.groupdict():
        val = tag_parser(t_match.group('args'))
      attributes.update({tag: val})
      ftext = ' '.join([ftext[:t_match.start()],
        ftext[t_match.end():]])

  attributes.update({ 'text': ftext })
  return attributes


  

  











