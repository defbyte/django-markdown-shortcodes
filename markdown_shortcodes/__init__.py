import itertools
import re

from django.template.loader import render_to_string


SHORTCODE_REGEX = re.compile(r'(\[\[([a-z-]+)(.*?)\]\])') # In the form [[command param param param]]

SHORTCODE_PARAMETER_REGEX = re.compile(
    r"""
    \s(?:                # Parameters are separated by spaces
        ([\w\d/-]+)  |   # Free-form URL slug identifier, like a YouTube ID
        (\d+)        |   # A number
        "(.+?)"          # A string surrounded by quotes
    )""",
    re.X
)

# Dictionary of shortcode functions
shortcodes = {}


# A decorator function to define a shortcode
def shortcode(func):
    shortcodes[func.__name__] = func
    return func


@shortcode
def shortcode_vimeo(*args):
    return render_to_string("shortcodes/vimeo.html", {
        'id': args[0],
        'title': args[1] if len(args) > 1 else '',
        'alternate_uri': args[2] if len(args) > 2 else '',
    })


def expand_shortcodes(document):
    
    matches = re.findall(SHORTCODE_REGEX, document)
    for result in matches:
        sequence = result[0]
        shortcode_name = result[1].replace("-", "_")
        method_name = "shortcode_%s" % shortcode_name
        parameters_match = re.findall(SHORTCODE_PARAMETER_REGEX, result[2])
        flattened_params = list(itertools.chain(*parameters_match))
        parameters = [item for item in flattened_params if item != '']
        
        # If we have a method defined for the shortcode, call it.
        # Otherwise, ignore the shortcode string and move on.
        shortcode_method = shortcodes.get(method_name, None)
        if shortcode_method:
            print "  Rendering shortcode `%s` with parameters %r" % (shortcode_name, parameters)
            html_string = shortcode_method(*parameters)
            document = document.replace(sequence, html_string)
        else:
            print "  shortcode `%s` not found" % shortcode_name
    
    return document

