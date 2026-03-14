from elem import Elem, Text
from elements import *


class Page:
	"""
	A Page class that builds and validates HTML documents.
	
	The Page takes a root Elem (typically Html) and provides:
	- is_valid(): Validates the HTML structure according to W3C standards
	- __str__(): Returns HTML string with doctype if root is Html
	- write_to_file(): Writes HTML to file with doctype if root is Html
	"""

	VALID_TAGS = {
		'html', 'head', 'body', 'title', 'meta', 'img',
		'table', 'th', 'tr', 'td', 'ul', 'ol', 'li',
		'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'
	}

	# Tags that must contain exactly one Text and only Text
	SINGLE_TEXT_ONLY = {'title', 'h1', 'h2', 'li', 'th', 'td'}

	# Tags that can only contain Text
	TEXT_ONLY = {'p'}

	# Tags that can contain Text or P elements
	TEXT_OR_P = {'span'}

	# Tags that can contain specific child types (Body, Div)
	BODY_DIV_CHILDREN = {'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span'}

	# Tags that must contain only Li elements
	LIST_PARENTS = {'ul', 'ol'}

	def __init__(self, root):
		"""
		Initialize Page with a root Elem.
		
		Args:
			root: An instance of a class inheriting from Elem
		"""
		if not isinstance(root, Elem):
			raise ValueError("root must be an instance of Elem or its subclasses")
		self.root = root

	def __str__(self):
		"""
		Return HTML string representation with doctype if root is Html.
		"""
		html_str = str(self.root)
		if self.root.tag == 'html':
			return '<!DOCTYPE html>\n' + html_str
		return html_str

	def write_to_file(self, filename):
		"""
		Write HTML to file with doctype if root is Html.
		
		Args:
			filename: Name of the file to write to
		"""
		with open(filename, 'w', encoding='utf-8') as f:
			f.write(str(self))

	def is_valid(self):
		"""
		Validate the HTML document structure.
		
		Returns:
			True if all validation rules are satisfied, False otherwise
		"""
		return self._validate_node(self.root)

	def _validate_node(self, node):
		"""
		Recursively validate a node and its children.
		
		Args:
			node: An Elem or Text instance to validate
			
		Returns:
			True if node and all descendants are valid, False otherwise
		"""
		# Text nodes are always valid
		if isinstance(node, Text):
			return True

		# Check if tag is valid
		if node.tag not in self.VALID_TAGS:
			return False

		# Validate children based on parent tag
		if node.tag == 'html':
			return self._validate_html(node)
		elif node.tag == 'head':
			return self._validate_head(node)
		elif node.tag == 'body':
			return self._validate_body(node)
		elif node.tag in self.SINGLE_TEXT_ONLY:
			return self._validate_single_text(node)
		elif node.tag == 'p':
			return self._validate_p(node)
		elif node.tag == 'span':
			return self._validate_span(node)
		elif node.tag in self.LIST_PARENTS:
			return self._validate_list(node)
		elif node.tag == 'table':
			return self._validate_table(node)
		elif node.tag == 'tr':
			return self._validate_tr(node)
		elif node.tag == 'div':
			return self._validate_div(node)
		elif node.tag in ('meta', 'img', 'hr', 'br'):
			# Self-closing tags should have no content
			return len(node.content) == 0

		# For any other tag, just validate its children
		return all(self._validate_node(child) for child in node.content)

	def _validate_html(self, node):
		"""Html must contain exactly Head then Body (in that order)."""
		if len(node.content) != 2:
			return False
		
		# First child must be Head
		if not isinstance(node.content[0], Elem) or node.content[0].tag != 'head':
			return False
		
		# Second child must be Body
		if not isinstance(node.content[1], Elem) or node.content[1].tag != 'body':
			return False
		
		# Validate both children
		return (self._validate_node(node.content[0]) and
				self._validate_node(node.content[1]))

	def _validate_head(self, node):
		"""Head must contain exactly one Title."""
		# Count title elements
		titles = [child for child in node.content
				  if isinstance(child, Elem) and child.tag == 'title']
		
		if len(titles) != 1:
			return False
		
		# Validate all children
		return all(self._validate_node(child) for child in node.content)

	def _validate_body(self, node):
		"""Body can only contain: H1, H2, Div, Table, Ul, Ol, Span, or Text."""
		for child in node.content:
			if isinstance(child, Text):
				continue
			elif isinstance(child, Elem):
				if child.tag not in self.BODY_DIV_CHILDREN | {'text'}:
					return False
				if not self._validate_node(child):
					return False
			else:
				return False
		return True

	def _validate_div(self, node):
		"""Div can only contain: H1, H2, Div, Table, Ul, Ol, Span, or Text."""
		# Same rules as Body
		return self._validate_body(node)

	def _validate_single_text(self, node):
		"""Title, H1, H2, Li, Th, Td must contain exactly one Text and only this Text."""
		if len(node.content) != 1:
			return False
		
		child = node.content[0]
		if not isinstance(child, Text):
			return False
		
		return True

	def _validate_p(self, node):
		"""P must only contain Text."""
		for child in node.content:
			if not isinstance(child, Text):
				return False
		return True

	def _validate_span(self, node):
		"""Span must only contain Text or some P."""
		for child in node.content:
			if isinstance(child, Text):
				continue
			elif isinstance(child, Elem):
				if child.tag != 'p':
					return False
				if not self._validate_node(child):
					return False
			else:
				return False
		return True

	def _validate_list(self, node):
		"""Ul and Ol must contain at least one Li and only Li."""
		if len(node.content) == 0:
			return False  # Must have at least one Li
		
		for child in node.content:
			if not isinstance(child, Elem) or child.tag != 'li':
				return False
			if not self._validate_node(child):
				return False
		
		return True

	def _validate_table(self, node):
		"""Table must only contain Tr and only some Tr."""
		if len(node.content) == 0:
			return False  # Must have at least one Tr
		
		for child in node.content:
			if not isinstance(child, Elem) or child.tag != 'tr':
				return False
			if not self._validate_node(child):
				return False
		
		return True

	def _validate_tr(self, node):
		"""Tr must contain at least one Th or Td and only Th or Td (mutually exclusive)."""
		if len(node.content) == 0:
			return False  # Must have at least one Th or Td
		
		has_th = False
		has_td = False
		
		for child in node.content:
			if not isinstance(child, Elem):
				return False
			
			if child.tag == 'th':
				has_th = True
				if has_td:
					return False  # Th and Td are mutually exclusive
			elif child.tag == 'td':
				has_td = True
				if has_th:
					return False  # Th and Td are mutually exclusive
			else:
				return False
			
			if not self._validate_node(child):
				return False
		
		return True


# ============================================================================
# COMPREHENSIVE TEST SUITE
# ============================================================================

if __name__ == '__main__':

	# Test 1: Valid simple HTML document
	print("Test 1: Valid simple HTML document")
	simple_page = Page(Html([
		Head(Title(Text("Hello"))),
		Body(H1(Text("Welcome")))
	]))
	assert simple_page.is_valid() == True, "Simple page should be valid"
	print("✓ Passed")
	print(simple_page)
	print()

	# Test 2: Valid complex HTML document with all element types
	print("Test 2: Valid complex HTML document")
	complex_page = Page(Html([
		Head([
			Title(Text("My Website")),
			Meta(charset="UTF-8")
		]),
		Body([
			H1(Text("Main Title")),
			H2(Text("Subtitle")),
			P(Text("This is a paragraph.")),
			Div([
				Span(Text("Important text")),
				P(Text("A paragraph in span"))
			]),
			Ul([
				Li(Text("Item 1")),
				Li(Text("Item 2")),
				Li(Text("Item 3"))
			]),
			Ol([
				Li(Text("First")),
				Li(Text("Second"))
			]),
			Table([
				Tr([
					Th(Text("Header 1")),
					Th(Text("Header 2"))
				]),
				Tr([
					Td(Text("Data 1")),
					Td(Text("Data 2"))
				])
			]),
			Hr(),
			Br(),
			Img(src="test.jpg")
		])
	]))
	assert complex_page.is_valid() == True, "Complex page should be valid"
	print("✓ Passed")
	print()

	# Test 3: Invalid - Html without Head
	print("Test 3: Invalid - Html without Head")
	invalid_html_no_head = Page(Html(Body(H1(Text("No head")))))
	assert invalid_html_no_head.is_valid() == False, "Should fail: no Head"
	print("✓ Correctly identified as invalid")
	print()

	# Test 4: Invalid - Html without Body
	print("Test 4: Invalid - Html without Body")
	invalid_html_no_body = Page(Html(Head(Title(Text("No body")))))
	assert invalid_html_no_body.is_valid() == False, "Should fail: no Body"
	print("✓ Correctly identified as invalid")
	print()

	# Test 5: Invalid - Head with multiple Titles
	print("Test 5: Invalid - Head with multiple Titles")
	invalid_multi_titles = Page(Html([
		Head([
			Title(Text("Title 1")),
			Title(Text("Title 2"))
		]),
		Body(H1(Text("Content")))
	]))
	assert invalid_multi_titles.is_valid() == False, "Should fail: multiple titles"
	print("✓ Correctly identified as invalid")
	print()

	# Test 6: Invalid - Title with multiple Text
	print("Test 6: Invalid - Title with multiple Text")
	invalid_multi_text_title = Page(Html([
		Head(Title([Text("Title"), Text("Extra")])),
		Body(H1(Text("Content")))
	]))
	assert invalid_multi_text_title.is_valid() == False, "Should fail: multiple texts in title"
	print("✓ Correctly identified as invalid")
	print()

	# Test 7: Invalid - Body with invalid child
	print("Test 7: Invalid - Body with invalid child")
	invalid_body_child = Page(Html([
		Head(Title(Text("Title"))),
		Body([
			H1(Text("Valid")),
			Table([Tr([Td(Text("Invalid in body without ul/ol context"))])]),
			Title(Text("Invalid in body"))  # Title not allowed in Body
		])
	]))
	# This should be valid since Table and H1 are allowed in Body
	# Let's create a truly invalid case
	invalid_body_child = Page(Html([
		Head(Title(Text("Title"))),
		Body(Meta(charset="utf-8"))  # Meta not allowed directly in Body
	]))
	assert invalid_body_child.is_valid() == False, "Should fail: invalid element in Body"
	print("✓ Correctly identified as invalid")
	print()

	# Test 8: Invalid - P with non-Text content
	print("Test 8: Invalid - P with non-Text content")
	invalid_p = Page(Html([
		Head(Title(Text("Title"))),
		Body(P(H1(Text("Invalid"))))  # H1 not allowed in P
	]))
	assert invalid_p.is_valid() == False, "Should fail: non-text in P"
	print("✓ Correctly identified as invalid")
	print()

	# Test 9: Invalid - Ul without Li
	print("Test 9: Invalid - Ul without Li")
	invalid_ul = Page(Html([
		Head(Title(Text("Title"))),
		Body(Ul(Text("Not a Li")))
	]))
	assert invalid_ul.is_valid() == False, "Should fail: Ul without Li"
	print("✓ Correctly identified as invalid")
	print()

	# Test 10: Invalid - Tr with mixed Th and Td
	print("Test 10: Invalid - Tr with mixed Th and Td")
	invalid_tr = Page(Html([
		Head(Title(Text("Title"))),
		Body(Table(Tr([
			Th(Text("Header")),
			Td(Text("Data"))  # Can't mix Th and Td
		])))
	]))
	assert invalid_tr.is_valid() == False, "Should fail: mixed Th and Td in Tr"
	print("✓ Correctly identified as invalid")
	print()

	# Test 11: Invalid - Table without Tr
	print("Test 11: Invalid - Table without Tr")
	invalid_table = Page(Html([
		Head(Title(Text("Title"))),
		Body(Table(Text("Not a Tr")))
	]))
	assert invalid_table.is_valid() == False, "Should fail: Table without Tr"
	print("✓ Correctly identified as invalid")
	print()

	# Test 12: String representation with doctype
	print("Test 12: String representation with doctype")
	page_with_doctype = Page(Html([
		Head(Title(Text("Test"))),
		Body(H1(Text("Hello")))
	]))
	html_str = str(page_with_doctype)
	assert html_str.startswith('<!DOCTYPE html>'), "Should have doctype"
	print("✓ Doctype correctly added")
	print()

	# Test 13: Write to file
	print("Test 13: Write to file")
	page = Page(Html([
		Head(Title(Text("File Test"))),
		Body(H1(Text("Content")))
	]))
	page.write_to_file('/tmp/test_page.html')
	with open('/tmp/test_page.html', 'r') as f:
		content = f.read()
		assert content.startswith('<!DOCTYPE html>'), "File should contain doctype"
		assert '<html>' in content, "File should contain html tag"
	print("✓ File written correctly")
	print()

	# Test 14: Invalid - Tr without Th/Td
	print("Test 14: Invalid - Tr without Th/Td")
	invalid_tr_empty = Page(Html([
		Head(Title(Text("Title"))),
		Body(Table(Tr(Text("Should have Th or Td"))))
	]))
	assert invalid_tr_empty.is_valid() == False, "Should fail: Tr without Th/Td"
	print("✓ Correctly identified as invalid")
	print()

	# Test 15: Invalid tag type
	print("Test 15: Invalid tag type detection")
	invalid_elem = Elem('invalid_tag', content=Text("test"))
	invalid_bad_tag = Page(Html([
		Head(Title(Text("Title"))),
		Body(invalid_elem)
	]))
	assert invalid_bad_tag.is_valid() == False, "Should fail: invalid tag"
	print("✓ Correctly identified invalid tag")
	print()

	# Test 16: Span with P content
	print("Test 16: Valid - Span with P content")
	valid_span_p = Page(Html([
		Head(Title(Text("Title"))),
		Body(Span([
			Text("Text before"),
			P(Text("Paragraph in span"))
		]))
	]))
	assert valid_span_p.is_valid() == True, "Span with P should be valid"
	print("✓ Passed")
	print()

	# Test 17: Div with nested content
	print("Test 17: Valid - Div with nested content")
	valid_nested_div = Page(Html([
		Head(Title(Text("Title"))),
		Body(Div([
			H1(Text("Heading")),
			Div([
				H2(Text("Subheading")),
				P(Text("Content"))
			])
		]))
	]))
	assert valid_nested_div.is_valid() == True, "Nested Div should be valid"
	print("✓ Passed")
	print()

	# Test 18: Invalid - Nested invalid tag
	print("Test 18: Invalid - Nested invalid tag")
	invalid_nested = Page(Html([
		Head(Title(Text("Title"))),
		Body(Div([
			H1(Text("Valid")),
			Elem('article', content=Text("Invalid tag"))
		]))
	]))
	assert invalid_nested.is_valid() == False, "Should fail: invalid nested tag"
	print("✓ Correctly identified as invalid")
	print()

	print("\n" + "="*50)
	print("ALL TESTS PASSED! ✓")
	print("="*50)
