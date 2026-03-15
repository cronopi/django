from elem import Elem


class Page:
	VALID_TAGS = {
		'html', 'head', 'body', 'title', 'meta', 'img', 'table',
		'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'
	}

	def __init__(self, elem):
		if not isinstance(elem, Elem):
			raise ValueError("Page must be initialized with an Elem instance")
		self.elem = elem

	def _check_head_valid(self, head):
		title_count = 0
		for child in head.content:
			if child.tag == 'title':
				title_count += 1
		return title_count == 1

	def _is_valid_body_div_child(self, child):
		allowed_tags = {'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span'}

		if isinstance(child, Elem):
			return child.tag in allowed_tags

		return False

	def _check_p_content(self, p_elem):
		for child in p_elem.content:
			# Si algún hijo es un Elem, es inválido
			if isinstance(child, Elem):
				return False
		return True

	def _check_span_content(self, span_elem):
		for child in span_elem.content:
			# Si es un Elem, solo puede ser P
			if isinstance(child, Elem):
				if child.tag != 'p':
					return False
		return True

	def _check_ul_ol_content(self, ul_ol_elem):
		if len(ul_ol_elem.content) == 0:
			return False

		for child in ul_ol_elem.content:
			if not isinstance(child, Elem) or child.tag != 'li':
				return False

		return True

	def _check_tr_content(self, tr_elem):
		if len(tr_elem.content) == 0:
			return False

		has_th = False
		has_td = False

		for child in tr_elem.content:
			if not isinstance(child, Elem):
				return False

			if child.tag == 'th':
				has_th = True
			elif child.tag == 'td':
				has_td = True
			else:
				return False

		if has_th and has_td:
			return False

		return True

	def _check_table_content(self, table_elem):
		"""Verifica que Table contenga al menos 1 Tr y SOLO Tr"""
		if len(table_elem.content) == 0:
			return False

		for child in table_elem.content:
			if not isinstance(child, Elem) or child.tag != 'tr':
				return False

		return True

	def _check_single_text_content(self, elem):
		if len(elem.content) != 1:
			return False
		if not isinstance(elem.content[0], str):
			return False
		return True

	def _validate_tree(self, root):
		single_text_tags = {'title', 'h1', 'h2', 'li', 'th', 'td'}

		nodes_to_check = [root]

		while nodes_to_check:
			node = nodes_to_check.pop(0)

			if isinstance(node, Elem):
				if node.tag in single_text_tags:
					if not self._check_single_text_content(node):
						return False

				if node.tag == 'p':
					if not self._check_p_content(node):
						return False

				if node.tag == 'span':
					if not self._check_span_content(node):
						return False

				if node.tag in {'ul', 'ol'}:
					if not self._check_ul_ol_content(node):
						return False

				if node.tag == 'tr':
					if not self._check_tr_content(node):
						return False
			if node.tag == 'table':
				if not self._check_table_content(node):
					return False
				for child in node.content:
					nodes_to_check.append(child)

		return True

	def is_valid(self):
		if self.elem.tag != 'html':
			return False

		if len(self.elem.content) != 2:
			return False

		if self.elem.content[0].tag != 'head':
			return False

		if self.elem.content[1].tag != 'body':
			return False

		if not self._check_head_valid(self.elem.content[0]):
			return False

		for child in self.elem.content[1].content:
			if not self._is_valid_body_div_child(child):
				return False

		if not self._validate_tree(self.elem):
			return False

		return True

	def __str__(self):
		"""Devuelve el HTML con doctype si el root es 'html'"""
		html_str = str(self.elem)

		# Agregar doctype si y solo si el root es 'html'
		if self.elem.tag == 'html':
			return '<!DOCTYPE html>\n' + html_str

		return html_str

	def write_to_file(self, filename):
		"""Escribe el HTML en un archivo con doctype si es necesario"""
		with open(filename, 'w') as f:
			f.write(str(self))


if __name__ == '__main__':
	from elements import Html, Head, Body, Title, H1, P, Div, Span, Ul, Li, Table, Tr, Th, Td

	# Crear un HTML completo y válido
	html = Html([
		Head([
			Title('Mi Página')
		]),
		Body([
			H1('Bienvenido'),
			Div([
				P('Este es un párrafo'),
				Span('Texto en span'),
				Ul([
					Li('Item 1'),
					Li('Item 2'),
					Li('Item 3')
				])
			]),
			Table([
				Tr([
					Th('Header 1'),
					Th('Header 2')
				]),
				Tr([
					Th('Header 3'),
					Th('Header 4')
				])
			])
		])
	])

	# Crear la página y validar
	page = Page(html)

	print("¿Es válido?", page.is_valid())
	print("\n--- HTML generado ---")
	print(page)
	print("\n--- Guardando en archivo ---")
	page.write_to_file('output.html')
	print("Guardado en output.html")
