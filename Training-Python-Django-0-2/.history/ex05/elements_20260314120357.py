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
	# Test 1: HTML structure from exercise description
	print("=" * 60)
	print("Test 1: HTML structure (from exercise)")
	print("=" * 60)
	doc = Html([
		Head(Title(Text("Hello ground!"))),
		Body([
			H1(Text("Oh no, not again!")),
			Img(src="http://i.imgur.com/pfp3T.jpg")
		])
	])
	print(doc)

	# Test 2: Simple elements with content
	print("\n" + "=" * 60)
	print("Test 2: Simple elements")
	print("=" * 60)
	print(H1(Text("Heading 1")))
	print(H2(Text("Heading 2")))
	print(P(Text("Paragraph")))
	print(Div(Text("Div content")))

	# Test 3: Lists
	print("\n" + "=" * 60)
	print("Test 3: Unordered List")
	print("=" * 60)
	ul = Ul([
		Li(Text("Item 1")),
		Li(Text("Item 2")),
		Li(Text("Item 3"))
	])
	print(ul)

	# Test 4: Table
	print("\n" + "=" * 60)
	print("Test 4: Table")
	print("=" * 60)
	table = Table([
		Tr([
			Th(Text("Name")),
			Th(Text("Age"))
		]),
		Tr([
			Td(Text("Alice")),
			Td(Text("25"))
		])
	])
	print(table)

	# Test 5: Self-closing tags
	print("\n" + "=" * 60)
	print("Test 5: Self-closing tags")
	print("=" * 60)
	print(Img(src="image.jpg", alt="alt text"))
	print(Hr())
	print(Br())

	# Test 6: Nested with attributes
	print("\n" + "=" * 60)
	print("Test 6: Elements with attributes")
	print("=" * 60)
	div_styled = Div(
		P(Text("Content")),
		id="main",
		class_="container"
	)
	print(div_styled)
