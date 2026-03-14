#!/usr/bin/env python3
# coding: utf-8


class Text(str):
	"""Clase que representa texto en HTML. Hereda de str."""
	
	def __new__(cls, content=''):
		"""Procesa el contenido antes de crear la instancia de str"""
		# Convertir a string por si es número u otro tipo
		content = str(content)
		
		# Escapar caracteres especiales htmll
		content = content.replace('&', '&amp;')
		content = content.replace('<', '&lt;')
		content = content.replace('>', '&gt;')
		content = content.replace('"', '&quot;')
		
		# Reemplazar saltos de línea con <br />
		content = content.replace('\n', '\n<br />\n')
		
		# Crear la instancia de str
		return str.__new__(cls, content)


class Elem:
	"""Clase que representa un elemento HTML"""
	
	class ValidationError(Exception):
		"""Excepción personalizada para errores de validación"""
		pass
	
	def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
		"""
		Constructor - el 'builder' del elemento HTML
		
		Args:
			tag: Nombre de la etiqueta (p.ej: 'div', 'body', 'h1')
			attr: Diccionario de atributos HTML (p.ej: {'src': 'imagen.jpg'})
			content: Contenido del elemento (Text, Elem, lista, o None)
			tag_type: 'simple' (auto-cierre como <img />) o 'double' (con cierre)
		"""
		self.tag = tag
		self.attr = attr if attr is not None else {}
		self.tag_type = tag_type
		self.content = []

