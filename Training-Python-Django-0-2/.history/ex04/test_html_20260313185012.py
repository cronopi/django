#!/usr/bin/env python3
"""Test script to generate the required HTML structure."""

from elem import Elem

# Create the HTML structure
html = Elem("html")

# Head section
head = Elem("head")
title = Elem("title")
title.add_content('"Hello ground!"')
head.add_content(title)
html.add_content(head)

# Body section
body = Elem("body")

# H1 element
h1 = Elem("h1")
h1.add_content('"Oh no, not again!"')
body.add_content(h1)

# Image element (self-closing)
img = Elem("img", attributes={"src": "http://i.imgur.com/pfp3T.jpg"}, type="simple")
body.add_content(img)

html.add_content(body)

# Print the result
print(str(html))
