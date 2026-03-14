#!/usr/bin/env python3
# coding: utf-8


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

