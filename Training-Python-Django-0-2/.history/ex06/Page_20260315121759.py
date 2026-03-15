from elem import Elem, Text


class Page:
	VALID_TAGS = {
		'html', 'head', 'body', 'title', 'meta', 'img', 'table',
		'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'
	}

	def __init__(self, elem):
		if not isinstance(elem, Elem):
			raise ValueError("Page must be initialized with an Elem instance")
		self.elem = elem

	def _check_valid_tags(self, node):
		"""
		REGLA 1: Validar que todos los tags en el árbol sean permitidos.
		Devuelve True si todos son válidos, False si alguno no lo es.
		"""
		# Un nodo puede ser Text o Elem
		if isinstance(node, Text):
			return True  # Text es siempre válido

		if isinstance(node, Elem):
			# Verificar que el tag de este nodo sea válido
			if node.tag not in self.VALID_TAGS:
				return False

			# Verificar recursivamente todos los hijos
			for child in node.content:
				if not self._check_valid_tags(child):
					return False

			return True

		return False

	def is_valid(self):
		# REGLA 1: Validar que todos los tags sean permitidos
		if not self._check_valid_tags(self.elem):
			return False

		return True
