from elem import Elem, Text
from elements import *


class Page:
	def __init__(self, root):
		if not isinstance(root, Elem):
			raise ValueError("root debe ser una instancia de Elem")
		self.root = root

	def __str__(self):
		"""
		Retorna el HTML con doctype si la raíz es 'html'.
		"""
		html_str = str(self.root)
		if self.root.tag == 'html':
			return '<!DOCTYPE html>\n' + html_str
		return html_str

	def write_to_file(self, filename):
		"""
		Escribe el HTML a un archivo con doctype si la raíz es 'html'.
		"""
		with open(filename, 'w', encoding='utf-8') as f:
			f.write(str(self))

	def is_valid(self):
		"""
		Valida la estructura del documento HTML.
		Retorna True si es válido, False en caso contrario.
		"""
		# TODO: Implementar validación
		return True
