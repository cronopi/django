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

		body = self.elem.content[1]
		for child in body.content:
			if not self._is_valid_body_div_child(child):
				return False

		return True
