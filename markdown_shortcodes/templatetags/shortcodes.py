from django import template

from markdown_shortcodes import expand_shortcodes

register = template.Library()

@register.filter
@stringfilter
def expand_shortcodes(val):
    return expand_shortcodes(val)
