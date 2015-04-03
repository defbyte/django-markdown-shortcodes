from markdown_shortcodes import shortcode, expand_shortcodes


doc = 'This is my document\nwhichhas a couple lines\nof text with an [[image 2740 "caption" "something else"]] shortcode\n\nand a video, we love vimeo [[vimeo 1x2c3v4]]'

print expand_shortcodes(doc)
