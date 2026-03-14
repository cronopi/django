from elem import Elem, Text


class Page:
	# Valid tags that can appear in HTML structure according to subject
	VALID_TAGS = {
		'html', 'head', 'body', 'title', 'meta', 'img', 'table', 
		'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'
	}
	
	def __init__(self, elem):
		if not isinstance(elem, Elem):
			raise ValueError("Page must be initialized with an Elem instance")
		self.elem = elem

	def is_valid(self):
		"""
		Validate the HTML tree structure.
		
		Returns:
			bool: True if valid according to all rules, False otherwise
		"""
		return self._validate_node(self.elem)
	
	def _validate_node(self, node):
		"""
		Recursively validate a node and its children.
		
		Args:
			node: The node to validate (Elem or Text)
			
		Returns:
			bool: True if node is valid
		"""
		# First check: if it's Text, it's always valid
		if isinstance(node, Text):
			return True
		
		# If it's not Text, it must be Elem
		if not isinstance(node, Elem):
			return False
		
		# Check 1: tag must be in VALID_TAGS
		tag = node.tag.lower()
		if tag not in self.VALID_TAGS:
			return False
		
		# TODO: Check tag-specific rules (next step)
		
		# Recursively validate all children
		for child in node.content:
			if not self._validate_node(child):
				return False
		
		return True
