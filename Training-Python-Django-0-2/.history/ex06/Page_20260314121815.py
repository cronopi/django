from elem import Elem, Text
from elements import *


class Page:
	"""
	Clase Page que construye y valida documentos HTML.
	El builder recibe una instancia de Elem.
	"""

	def __init__(self, root):
		"""
		Constructor: recibe un elemento Elem como raíz.
		
		Args:
			root: Una instancia de Elem o sus subclases
		"""
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


# ============================================================================
# PRUEBAS - TESTS
# ============================================================================

if __name__ == '__main__':
	print("Test 1: Crear una página simple")
	page = Page(Html([
		Head(Title(Text("Hola"))),
		Body(H1(Text("Bienvenido")))
	]))
	print("✓ Página creada")
	print()

	print("Test 2: Ver el HTML con doctype")
	print(page)
	print()

	print("Test 3: Escribir a archivo")
	page.write_to_file('/tmp/test.html')
	print("✓ Archivo creado: /tmp/test.html")
