#!/usr/bin/env python3
# coding: utf-8

from elem import Elem, Text

# Crear la estructura HTML especificada en el ejercicio
# <html>
#   <head>
#     <title>
#       "Hello ground!"
#     </title>
#   </head>
#   <body>
#     <h1>
#       "Oh no, not again!"
#     </h1>
#     <img src="http://i.imgur.com/pfp3T.jpg" />
#   </body>
# </html>

# Crear el elemento <title> con su contenido
title = Elem('title', content=Text('"Hello ground!"'))

# Crear el elemento <head> que contiene el <title>
head = Elem('head', content=title)

# Crear el elemento <h1> con su contenido
h1 = Elem('h1', content=Text('"Oh no, not again!"'))

# Crear el elemento <img> con atributo src (tag simple/self-closing)
img = Elem('img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')

# Crear el elemento <body> que contiene <h1> e <img>
body = Elem('body', content=[h1, img])

# Crear el elemento <html> que contiene <head> y <body>
html = Elem('html', content=[head, body])

# Mostrar el resultado
print(html)
