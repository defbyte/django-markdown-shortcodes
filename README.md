# Markdown Shortcodes for Django

Provides the ability to use WordPress-like "shortcodes" in your content, which get rendered as HTML.

The idea here is to extend Markdown authoring capabilities. For example, rendering a more complex component in the flow of a content body that shows featured content - or as simple as rendering a full-width Vimeo video.

This package does not come with a host of shortcodes defined, given these will be highly project-specific.

Instead, it provides a registration system (via a tiny decorator), the shortcode processor, and a template filter for convenience.

## Installation

Install via pip:

    pip install django-markdown-shortcodes

Please add `markdown_shortcodes` to `INSTALLED_APPS` in your Django project's settings.


## Defining Shortcodes

Shortcode functions names expected to start with `shortcode_` followed by the string/name that appears in your content.

The following example creates support for a `[[youtube]]` shortcode.

Define the processing function, using the `shortcode` decorator to register the function for processing:

    from markdown_shortcodes import shortcode

    @shortcode
    def shortcode_youtube(*args):
        return render_to_string("shortcodes/youtube.html", {
            'id': args[0],
            'title': args[1] if len(args) > 1 else '',
            'alternate_uri': args[2] if len(args) > 2 else '',
        })

Create a template file:

    <div class="shortcode-block">
      <div class="fluid-iframe -ratio-16-9">
        <iframe src="//www.youtube.com/embed/#{{ id }}"
          title="{{ title }}"
          frameborder="0"
          webkitallowfullscreen
          mozallowfullscreen
          allowfullscreen>
          This video requires an frame-capable browser.
          {% if alternate_uri %}
            <a href="{{ alternate_uri }}">See alternative content for {{ title }}</a>
          {% else %}
            <a href="https://www.youtube.com/watch?v=#{{ id }}">Watch {{ title }} on YouTube</a>
          {% endif %}
        </iframe>
      </div>
    </div>

Your content:

    So did you know about Whoa McTuggins? I saw an interview with him about preparing tomatos. It changed my life:
    
    [[youtube XTJIGGBN8l4 "A thrilling exploration of tomato dicing"]]
    
    Now I prepare pico de gallo almost weekly!


And in your content's template, something like this (`expand_shortcodes` is a provided by this package):

    ...
    {% load shortcodes %}
    
    <div class="Post-BodyText -u-awesome">
    {{ post.body|expand_shortcodes|safe|your_markdown_filter }}
    </div>
    
    ...
