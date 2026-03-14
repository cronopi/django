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
	
	def __str__(self):
		"""Genera el código HTML completo del elemento"""
		
		# Construir string de atributos HTML
		attr_str = ''
		for key, value in self.attr.items():
			attr_str += f' {key}="{value}"'
		
		# Tags simples (self-closing, como <img />)
		if self.tag_type == 'simple':
			return f'<{self.tag}{attr_str} />'
		
		# Tags dobles sin contenido
		if not self.content:
			return f'<{self.tag}{attr_str}></{self.tag}>'
		
		# Tags dobles con contenido (indentado con 2 espacios)
		content_lines = []
		for item in self.content:
			item_str = str(item)
			for line in item_str.split('\n'):
				content_lines.append('  ' + line)
		
		content_str = '\n' + '\n'.join(content_lines) + '\n'
		return f'<{self.tag}{attr_str}>{content_str}</{self.tag}>'
	
	def add_content(self, content):
		"""Agrega contenido al elemento. Solo acepta Text o Elem."""
		
		# Si es una lista, procesar cada elemento
		if isinstance(content, list):
			for item in content:
				if not isinstance(item, (Text, Elem)):
					raise Elem.ValidationError(
						f"Content must be Text or Elem, got {type(item).__name__}"
					)
				# No agregar Text vacío
				if isinstance(item, Text) and str(item) == '':
					continue
				self.content.append(item)
		
		# Si es un item único
		elif isinstance(content, (Text, Elem)):
			# No agregar Text vacío
			if isinstance(content, Text) and str(content) == '':
				return
			self.content.append(content)
		
		# Si no es válido, lanzar excepción
		else:
			raise Elem.ValidationError(
				f"Content must be Text or Elem, got {type(content).__name__}"
			)

