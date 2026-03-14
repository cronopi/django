from elem import Elem


class Page:
	def __init__(self, elem):
		if not isinstance(elem, Elem):
			raise ValueError("Page must be initialized with an Elem instance")
		self.elem = elem

	def is_valid(self):
		return True
