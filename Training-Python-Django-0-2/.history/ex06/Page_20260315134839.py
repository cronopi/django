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
		"""Verifica que Tr contenga al menos 1 Th o Td, SOLO esos, y no mezclar"""
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
		
		# No pueden estar mezclados
		if has_th and has_td:
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
