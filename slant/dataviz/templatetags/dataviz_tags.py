# dataviz_tags.py

from django.template import Context, Template
from django import template
import markdown

register = template.Library()


class RenderCustom(template.Node):

    @classmethod
    def handle_token(cls, parser, token):
        tokens = token.split_contents()
        field = tokens[1]
        return cls(parser.compile_filter(field))

    def __init__(self, field):
        self.field = field

    def render(self, context):
        render_field = self.field.resolve(context)
        render_template = Template(render_field)

        # 1. Render the template (with tags) into HTML. This resolves URLs,
        #    finds static resources, and does any other Django template magic.
        rendered = render_template.render(Context())

        # 2. Evaluate any shortcodes in the text.

        # 3. Render the result as markdown. This renders the main text into
        #    HTML with standard MD rules (headers, lists, emphasis, etc),
        #    ignoring any raw HTML.
        rendered = markdown.markdown(rendered)

        return rendered


def render_this(parser, token):
    return RenderCustom.handle_token(parser, token)


# Register tags
register.tag("render_this", render_this)
