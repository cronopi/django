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
	# Comprehensive test with all classes
	print("=" * 60)
	print("Complete HTML Document Test (All Classes)")
	print("=" * 60)

	doc = Html([
		Head([
			Title(Text("My Website")),
			Meta(name="charset", content="UTF-8"),
			Meta(name="viewport", content="width=device-width")
		]),
		Body([
			H1(Text("Welcome to My Site")),
			Hr(),

			# Section with paragraph and span
			Div([
				H2(Text("Introduction")),
				P([
					Text("This is a "),
					Span(Text("comprehensive"), id="highlight"),
					Text(" test of all HTML elements.")
				]),
				Br()
			]),

			# Lists
			H2(Text("Features:")),
			Ul([
				Li(Text("Simple inheritance pattern")),
				Li(Text("Easy to use elements")),
				Li(Text("Clean HTML output"))
			]),

			H2(Text("Steps:")),
			Ol([
				Li(Text("First step")),
				Li(Text("Second step")),
				Li(Text("Third step"))
			]),

			# Table
			H2(Text("Data Table:")),
			Table([
				Tr([
					Th(Text("Element")),
					Th(Text("Type")),
					Th(Text("Purpose"))
				]),
				Tr([
					Td(Text("Html")),
					Td(Text("double")),
					Td(Text("Root element"))
				]),
				Tr([
					Td(Text("Img")),
					Td(Text("simple")),
					Td(Text("Images"))
				]),
				Tr([
					Td(Text("Hr")),
					Td(Text("simple")),
					Td(Text("Horizontal rule"))
				])
			]),

			Br(),
			Hr(),

			# Mixed elements
			Div([
				P(Text("Some content with an image:")),
				Img(src="http://i.imgur.com/pfp3T.jpg", alt="Example image"),
				P(Text("And some final text."))
			], class_="container", id="main-content")
		])
	])

	print(doc)
