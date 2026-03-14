from elem import Elem, Text


class Html(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('html', attr=attr, content=content, tag_type='double')


class Head(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('head', attr=attr, content=content, tag_type='double')


class Body(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('body', attr=attr, content=content, tag_type='double')


class Title(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('title', attr=attr, content=content, tag_type='double')


class Meta(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('meta', attr=attr, content=content, tag_type='simple')


class Img(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('img', attr=attr, content=content, tag_type='simple')


class Table(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('table', attr=attr, content=content, tag_type='double')


class Th(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('th', attr=attr, content=content, tag_type='double')


class Tr(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('tr', attr=attr, content=content, tag_type='double')


class Td(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('td', attr=attr, content=content, tag_type='double')


class Ul(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('ul', attr=attr, content=content, tag_type='double')


class Ol(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('ol', attr=attr, content=content, tag_type='double')


class Li(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('li', attr=attr, content=content, tag_type='double')


class H1(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('h1', attr=attr, content=content, tag_type='double')


class H2(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('h2', attr=attr, content=content, tag_type='double')


class P(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('p', attr=attr, content=content, tag_type='double')


class Div(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('div', attr=attr, content=content, tag_type='double')


class Span(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('span', attr=attr, content=content, tag_type='double')


class Hr(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('hr', attr=attr, content=content, tag_type='simple')


class Br(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('br', attr=attr, content=content, tag_type='simple')


if __name__ == '__main__':
	# Test Suite - Demonstrate all classes

	# Test 1: Simple nested structure (from exercise description)
	print("=" * 50)
	print("Test 1: HTML structure from exercise")
	print("=" * 50)
	doc1 = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			H1(Text("Oh no, not again!")),
			Img(src="http://i.imgur.com/pfp3T.jpg")
		])
	])
	print(doc1)

	# Test 2: Basic HTML elements
	print("\n" + "=" * 50)
	print("Test 2: Basic HTML elements")
	print("=" * 50)
	print(H1(Text("Heading 1")))
	print(H2(Text("Heading 2")))
	print(P(Text("This is a paragraph")))
	print(Div(Text("This is a div")))
	print(Span(Text("This is a span")))

	# Test 3: Lists
	print("\n" + "=" * 50)
	print("Test 3: Unordered and Ordered Lists")
	print("=" * 50)
	ul = Ul([
		Li(Text("Item 1")),
		Li(Text("Item 2")),
		Li(Text("Item 3"))
	])
	print(ul)

	ol = Ol([
		Li(Text("First")),
		Li(Text("Second")),
		Li(Text("Third"))
	])
	print(ol)

	# Test 4: Table
	print("\n" + "=" * 50)
	print("Test 4: Table")
	print("=" * 50)
	table = Table([
		Tr([
			Th(Text("Name")),
			Th(Text("Age")),
			Th(Text("City"))
		]),
		Tr([
			Td(Text("Alice")),
			Td(Text("25")),
			Td(Text("NYC"))
		]),
		Tr([
			Td(Text("Bob")),
			Td(Text("30")),
			Td(Text("LA"))
		])
	])
	print(table)

	# Test 5: Simple tags (self-closing)
	print("\n" + "=" * 50)
	print("Test 5: Simple/Self-closing tags")
	print("=" * 50)
	print(Img(src="image.jpg", alt="An image"))
	print(Br())
	print(Hr())
	print(Meta(name="viewport", content="width=device-width"))

	# Test 6: Nested elements with attributes
	print("\n" + "=" * 50)
	print("Test 6: Elements with attributes")
	print("=" * 50)
	div_with_class = Div(
		P(Text("Styled paragraph")),
		id="main-div",
		class_="container"
	)
	print(div_with_class)

	# Test 7: Complex nested structure
	print("\n" + "=" * 50)
	print("Test 7: Complex nested structure")
	print("=" * 50)
	complex_doc = Html([
		Head([
			Title(Text("My Website")),
			Meta(name="charset", content="UTF-8")
		]),
		Body([
			H1(Text("Welcome")),
			P(Text("This is a complex example")),
			Div([
				H2(Text("Articles")),
				Ul([
					Li(Text("Article 1")),
					Li(Text("Article 2")),
				])
			]),
			Hr(),
			Footer(Text("Copyright 2026"))
		])
	])
	print(complex_doc)


class Footer(Elem):
	"""Footer element - added for completeness in tests"""
	def __init__(self, content=None, **attr):
		super().__init__('footer', attr=attr, content=content, tag_type='double')
