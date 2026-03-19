from elem import Elem

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

class Table(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('table', attr=attr, content=content, tag_type='double')

class Tr(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('tr', attr=attr, content=content, tag_type='double')

class Td(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('td', attr=attr, content=content, tag_type='double')

class H4(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('h4', attr=attr, content=content, tag_type='double')

class Ul(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('ul', attr=attr, content=content, tag_type='double')

class Li(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('li', attr=attr, content=content, tag_type='double')

class Meta(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('meta', attr=attr, content=content, tag_type='simple')
