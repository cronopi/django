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
		"""Verifica que el head contenga exactamente 1 title"""
		title_count = 0
		for child in head.content:
			if child.tag == 'title':
				title_count += 1
		return title_count == 1

	def is_valid(self):
		if self.elem.tag != 'html':
			return False

		if len(self.elem.content) != 2:
			return False

		if self.elem.content[0].tag != 'head':
			return False

		if self.elem.content[1].tag != 'body':
			return False

		return True
