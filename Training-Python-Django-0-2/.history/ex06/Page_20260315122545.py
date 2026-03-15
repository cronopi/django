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

	def is_valid(self):
		# Verificar que el root sea 'html'
		if self.elem.tag != 'html':
			return False
		
		# Verificar que html tenga exactamente 2 hijos
		if len(self.elem.content) != 2:
			return False
		
		# Verificar que el primer hijo sea 'head'
		if self.elem.content[0].tag != 'head':
			return False
		
		# Verificar que el segundo hijo sea 'body'
		if self.elem.content[1].tag != 'body':
			return False
		
		return True
