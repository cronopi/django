from elem import Elem, Text
from elements import *


class Page:
	"""
	Clase Page que construye y valida documentos HTML.
	
	- Constructor: recibe una instancia de Elem
	- is_valid(): valida la estructura HTML
	- __str__(): retorna HTML con doctype si la raíz es Html
	- write_to_file(): escribe HTML a archivo
	"""

	# Lista de todos los tags HTML válidos
	VALID_TAGS = {
		'html', 'head', 'body', 'title', 'meta', 'img',
		'table', 'th', 'tr', 'td', 'ul', 'ol', 'li',
		'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'
	}

	def __init__(self, root):
		"""
		Inicializa Page con un elemento raíz.
		
		Args:
			root: Una instancia de Elem o sus subclases
		"""
		if not isinstance(root, Elem):
			raise ValueError("root debe ser una instancia de Elem o sus subclases")
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
		
		Args:
			filename: Nombre del archivo
		"""
		with open(filename, 'w', encoding='utf-8') as f:
			f.write(str(self))

	def is_valid(self):
		"""
		Valida la estructura del documento HTML.
		
		Retorna:
			True si cumple todas las reglas, False en caso contrario
		"""
		# Primero: verifica que todos los tags sean válidos
		if not self._all_tags_valid(self.root):
			return False
		
		# Segundo: valida la estructura específica
		return self._validate_structure(self.root)

	def _all_tags_valid(self, node):
		"""
		Verifica que todos los nodos tengan tags válidos.
		"""
		if isinstance(node, Text):
			return True
		
		# Verifica si el tag es válido
		if node.tag not in self.VALID_TAGS:
			return False
		
		# Verifica recursivamente los hijos
		for child in node.content:
			if not self._all_tags_valid(child):
				return False
		
		return True

	def _validate_structure(self, node):
		"""
		Valida las reglas de estructura específicas de cada tag.
		"""
		if isinstance(node, Text):
			return True
		
		# Aplica reglas según el tag
		if node.tag == 'html':
			return self._validate_html(node)
		elif node.tag == 'head':
			return self._validate_head(node)
		elif node.tag == 'body':
			return self._validate_body(node)
		elif node.tag == 'title':
			return self._validate_title(node)
		elif node.tag in ('h1', 'h2', 'li', 'th', 'td'):
			return self._validate_single_text(node)
		elif node.tag == 'p':
			return self._validate_p(node)
		elif node.tag == 'span':
			return self._validate_span(node)
		elif node.tag in ('ul', 'ol'):
			return self._validate_list(node)
		elif node.tag == 'table':
			return self._validate_table(node)
		elif node.tag == 'tr':
			return self._validate_tr(node)
		elif node.tag == 'div':
			return self._validate_div(node)
		elif node.tag in ('meta', 'img', 'hr', 'br'):
			# Tags de autocierre no deben tener contenido
			return len(node.content) == 0
		
		return True

	def _validate_html(self, node):
		"""
		Html debe contener exactamente: primero Head, luego Body.
		"""
		if len(node.content) != 2:
			return False
		
		# Primer hijo debe ser Head
		first = node.content[0]
		if not isinstance(first, Elem) or first.tag != 'head':
			return False
		
		# Segundo hijo debe ser Body
		second = node.content[1]
		if not isinstance(second, Elem) or second.tag != 'body':
			return False
		
		# Valida recursivamente
		return (self._validate_structure(first) and
				self._validate_structure(second))

	def _validate_head(self, node):
		"""
		Head debe contener exactamente un Title.
		"""
		titles = [c for c in node.content 
				  if isinstance(c, Elem) and c.tag == 'title']
		
		if len(titles) != 1:
			return False
		
		# Valida todos los hijos
		for child in node.content:
			if not self._validate_structure(child):
				return False
		
		return True

	def _validate_title(self, node):
		"""
		Title debe contener exactamente un Text.
		"""
		if len(node.content) != 1:
			return False
		
		if not isinstance(node.content[0], Text):
			return False
		
		return True

	def _validate_body(self, node):
		"""
		Body puede contener: H1, H2, Div, Table, Ul, Ol, Span, o Text.
		"""
		allowed_tags = {'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span'}
		
		for child in node.content:
			if isinstance(child, Text):
				continue
			elif isinstance(child, Elem):
				if child.tag not in allowed_tags:
					return False
				if not self._validate_structure(child):
					return False
			else:
				return False
		
		return True

	def _validate_div(self, node):
		"""
		Div tiene las mismas reglas que Body.
		"""
		return self._validate_body(node)

	def _validate_single_text(self, node):
		"""
		H1, H2, Li, Th, Td deben contener exactamente un Text.
		"""
		if len(node.content) != 1:
			return False
		
		if not isinstance(node.content[0], Text):
			return False
		
		return True

	def _validate_p(self, node):
		"""
		P debe contener solo Text.
		"""
		for child in node.content:
			if not isinstance(child, Text):
				return False
		
		return True

	def _validate_span(self, node):
		"""
		Span puede contener Text o elementos P.
		"""
		for child in node.content:
			if isinstance(child, Text):
				continue
			elif isinstance(child, Elem):
				if child.tag != 'p':
					return False
				if not self._validate_structure(child):
					return False
			else:
				return False
		
		return True

	def _validate_list(self, node):
		"""
		Ul y Ol deben contener al menos un Li, solo Li.
		"""
		if len(node.content) == 0:
			return False
		
		for child in node.content:
			if not isinstance(child, Elem) or child.tag != 'li':
				return False
			if not self._validate_structure(child):
				return False
		
		return True

	def _validate_table(self, node):
		"""
		Table debe contener solo Tr (al menos uno).
		"""
		if len(node.content) == 0:
			return False
		
		for child in node.content:
			if not isinstance(child, Elem) or child.tag != 'tr':
				return False
			if not self._validate_structure(child):
				return False
		
		return True

	def _validate_tr(self, node):
		"""
		Tr debe contener Th o Td (mutuamente excluyentes, al menos uno).
		"""
		if len(node.content) == 0:
			return False
		
		has_th = False
		has_td = False
		
		for child in node.content:
			if not isinstance(child, Elem):
				return False
			
			if child.tag == 'th':
				has_th = True
			elif child.tag == 'td':
				has_td = True
			else:
				return False
			
			# No pueden mezclarse Th y Td
			if has_th and has_td:
				return False
			
			if not self._validate_structure(child):
				return False
		
		return True


# ============================================================================
# PRUEBAS - TESTS
# ============================================================================

if __name__ == '__main__':
	print("="*60)
	print("PRUEBAS DEL PAGE CLASS")
	print("="*60)
	print()

	# Test 1: Verificar que se crea correctamente
	print("Test 1: Crear una página válida simple")
	page1 = Page(Html([
		Head(Title(Text("Mi primera página"))),
		Body(H1(Text("¡Hola mundo!")))
	]))
	print("✓ Página creada exitosamente")
	print()

	# Test 2: Ver el HTML con doctype
	print("Test 2: Ver el HTML generado con doctype")
	print(page1)
	print()

	# Test 3: Validar estructura correcta
	print("Test 3: Validar estructura correcta")
	assert page1.is_valid() == True, "La página debe ser válida"
	print("✓ La página es válida")
	print()

	# Test 4: Detectar HTML sin Head
	print("Test 4: Detectar HTML sin Head (inválido)")
	page_sin_head = Page(Html(Body(H1(Text("Sin head")))))
	assert page_sin_head.is_valid() == False, "Debe fallar sin Head"
	print("✓ Correctamente identificado como inválido")
	print()

	# Test 5: Detectar Head sin Title
	print("Test 5: Detectar Head sin Title (inválido)")
	page_sin_title = Page(Html([
		Head(Meta(charset="utf-8")),
		Body(H1(Text("Sin title")))
	]))
	assert page_sin_title.is_valid() == False, "Debe fallar sin Title"
	print("✓ Correctamente identificado como inválido")
	print()

	# Test 6: Escribir a archivo
	print("Test 6: Escribir HTML a archivo")
	page1.write_to_file('/tmp/mi_pagina.html')
	with open('/tmp/mi_pagina.html', 'r') as f:
		contenido = f.read()
		assert '<!DOCTYPE html>' in contenido, "Debe tener doctype"
	print("✓ Archivo creado correctamente: /tmp/mi_pagina.html")
	print()

	# Test 7: Página más compleja
	print("Test 7: Página más compleja con varios elementos")
	page2 = Page(Html([
		Head(Title(Text("Página Compleja"))),
		Body([
			H1(Text("Título Principal")),
			H2(Text("Subtítulo")),
			P(Text("Este es un párrafo de texto.")),
			Div([
				Span(Text("Texto importante")),
				P(Text("Un párrafo dentro de un span"))
			]),
			Ul([
				Li(Text("Elemento 1")),
				Li(Text("Elemento 2"))
			])
		])
	]))
	assert page2.is_valid() == True, "Página compleja debe ser válida"
	print("✓ Página compleja es válida")
	print()

	print("="*60)
	print("¡TODOS LOS TESTS PASARON! ✓")
	print("="*60)
