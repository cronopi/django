from elem import Text, Elem
from elements import (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td,
                      Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br)


class Page:
	"""
	Page class that wraps an Elem instance (typically Html root) and provides
	validation and HTML export functionality.
	"""
	
	# Valid tags that can appear in the HTML tree
	VALID_TAGS = {
		'html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr', 'td',
		'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'
	}
	
	def __init__(self, elem):
		"""
		Initialize Page with an Elem instance.
		
		Args:
			elem: An instance of Elem (or its subclasses like Html, Head, etc.)
		"""
		if not isinstance(elem, Elem):
			raise ValueError("Page must be initialized with an Elem instance")
		self.elem = elem
	
	def is_valid(self):
		"""
		Validate the HTML structure against the specified rules.
		
		Validation rules:
		1. All nodes must have valid tags or be Text
		2. Html must contain Head, then Body (exactly in that order)
		3. Head must contain exactly one Title
		4. Body and Div can only contain: H1, H2, Div, Table, Ul, Ol, Span, or Text
		5. Title, H1, H2, Li, Th, Td can only contain one Text (exactly)
		6. P can only contain Text
		7. Span can only contain Text or some P
		8. Ul and Ol must contain at least one Li (and only Li)
		9. Tr must contain Th or Td (at least one), and they must be mutually exclusive
		10. Table must contain only Tr (and only some Tr)
		
		Returns:
			bool: True if valid, False otherwise
		"""
		return self._validate_node(self.elem)
	
	def _validate_node(self, node, parent_tag=None):
		"""
		Recursively validate a node and its children.
		
		Args:
			node: The node to validate (Elem or Text)
			parent_tag: The tag name of the parent node
			
		Returns:
			bool: True if node and all children are valid
		"""
		# Rule 1: Check if node type is valid
		if isinstance(node, Text):
			return True  # Text is always valid
		
		if not isinstance(node, Elem):
			return False
		
		tag = node.tag.lower()
		
		# Rule 1: All tags must be in VALID_TAGS
		if tag not in self.VALID_TAGS:
			return False
		
		# Apply parent-specific rules based on parent_tag
		if parent_tag:
			if not self._validate_parent_child_relationship(parent_tag, tag):
				return False
		
		# Apply tag-specific content rules
		if not self._validate_tag_content(node):
			return False
		
		# Recursively validate children
		for child in node.content:
			if not self._validate_node(child, parent_tag=tag):
				return False
		
		return True
	
	def _validate_tag_content(self, node):
		"""
		Validate that a node's content follows tag-specific rules.
		
		Args:
			node: The Elem node to validate
			
		Returns:
			bool: True if content is valid for this tag
		"""
		tag = node.tag.lower()
		content = node.content
		
		# Rule 2: Html must strictly contain Head, then Body
		if tag == 'html':
			if len(content) != 2:
				return False
			if not isinstance(content[0], Elem) or content[0].tag.lower() != 'head':
				return False
			if not isinstance(content[1], Elem) or content[1].tag.lower() != 'body':
				return False
			return True
		
		# Rule 3: Head must contain exactly one Title
		if tag == 'head':
			title_count = 0
			for child in content:
				if isinstance(child, Elem):
					if child.tag.lower() == 'title':
						title_count += 1
					# Head can contain Title and Meta
					if child.tag.lower() not in ('title', 'meta'):
						return False
				elif isinstance(child, Text):
					# Only empty Text is allowed (whitespace)
					if str(child).strip():
						return False
			return title_count == 1
		
		# Rule 4: Body can only contain H1, H2, Div, Table, Ul, Ol, Span, or Text
		if tag == 'body':
			allowed_children = {'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span'}
			for child in content:
				if isinstance(child, Elem):
					if child.tag.lower() not in allowed_children:
						return False
				elif isinstance(child, Text):
					# Only empty Text is allowed
					if str(child).strip():
						return False
			return True
		
		# Rule 4b: Div can only contain H1, H2, Div, Table, Ul, Ol, Span, or Text
		if tag == 'div':
			allowed_children = {'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span'}
			for child in content:
				if isinstance(child, Elem):
					if child.tag.lower() not in allowed_children:
						return False
				elif isinstance(child, Text):
					# Only empty Text is allowed
					if str(child).strip():
						return False
			return True
		
		# Rule 5: Title, H1, H2, Li, Th, Td must contain exactly one Text
		if tag in ('title', 'h1', 'h2', 'li', 'th', 'td'):
			if len(content) != 1:
				return False
			if not isinstance(content[0], Text):
				return False
			return True
		
		# Rule 6: P must contain only Text
		if tag == 'p':
			if len(content) != 1:
				return False
			if not isinstance(content[0], Text):
				return False
			return True
		
		# Rule 7: Span can contain Text or some P elements
		if tag == 'span':
			for child in content:
				if isinstance(child, Elem):
					if child.tag.lower() != 'p':
						return False
				elif not isinstance(child, Text):
					return False
			return True
		
		# Rule 8: Ul and Ol must contain at least one Li and only Li
		if tag in ('ul', 'ol'):
			if len(content) == 0:
				return False
			for child in content:
				if isinstance(child, Elem):
					if child.tag.lower() != 'li':
						return False
				elif isinstance(child, Text):
					# Only empty Text is allowed
					if str(child).strip():
						return False
			return True
		
		# Rule 9: Tr must contain Th or Td (at least one) and be mutually exclusive
		if tag == 'tr':
			if len(content) == 0:
				return False
			has_th = False
			has_td = False
			for child in content:
				if isinstance(child, Elem):
					child_tag = child.tag.lower()
					if child_tag == 'th':
						has_th = True
					elif child_tag == 'td':
						has_td = True
					elif not isinstance(child, Text):
						return False
				elif isinstance(child, Text):
					# Only empty Text is allowed
					if str(child).strip():
						return False
			# Th and Td must be mutually exclusive
			return has_th != has_td  # XOR: one must be true, but not both
		
		# Rule 10: Table must contain only Tr
		if tag == 'table':
			if len(content) == 0:
				return False
			for child in content:
				if isinstance(child, Elem):
					if child.tag.lower() != 'tr':
						return False
				elif isinstance(child, Text):
					# Only empty Text is allowed
					if str(child).strip():
						return False
			return True
		
		# Meta and Img are self-closing with no content
		if tag in ('meta', 'img'):
			return len(content) == 0
		
		# Hr and Br are self-closing with no content
		if tag in ('hr', 'br'):
			return len(content) == 0
		
		return True
	
	def _validate_parent_child_relationship(self, parent_tag, child_tag):
		"""
		Validate parent-child relationships (complementary to _validate_tag_content).
		
		Args:
			parent_tag: The parent element's tag
			child_tag: The child element's tag
			
		Returns:
			bool: True if relationship is valid
		"""
		# This is handled by _validate_tag_content, so return True
		return True
	
	def __str__(self):
		"""
		Return HTML string with doctype if root is Html.
		
		Returns:
			str: The HTML representation with doctype prepended if applicable
		"""
		html_content = str(self.elem)
		
		# Add doctype if root element is Html
		if self.elem.tag.lower() == 'html':
			return '<!DOCTYPE html>\n' + html_content
		
		return html_content
	
	def write_to_file(self, filename):
		"""
		Write the HTML code to a file with doctype if root is Html.
		
		Args:
			filename: The name of the file to write to
		"""
		html_content = str(self)
		
		try:
			with open(filename, 'w', encoding='utf-8') as f:
				f.write(html_content)
		except IOError as e:
			raise IOError(f"Failed to write to file {filename}: {e}")


if __name__ == '__main__':
	print("Page class ready for testing!")
