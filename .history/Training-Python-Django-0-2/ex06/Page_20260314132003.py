from elem import Text, Elem


class Page:
	"""
	Page class that wraps an Elem instance (typically Html root).

	According to the subject:
	- The builder (constructor) takes an instance of a class inheriting Elem
	- It must implement is_valid() method to validate HTML structure
	"""

	def __init__(self, elem):
		"""
		Initialize Page with an Elem instance.

		Args:
			elem: An instance of Elem (or its subclasses)

		Raises:
			ValueError: If elem is not an instance of Elem
		"""
		if not isinstance(elem, Elem):
			raise ValueError("Page must be initialized with an Elem instance")
		self.elem = elem

	def is_valid(self):
		return True
