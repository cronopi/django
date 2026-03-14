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

class table(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('table', attr=attr, content=content, tag_type='double')

class th(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('th', attr=attr, content=content, tag_type='double')

class tr(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('tr', attr=attr, content=content, tag_type='double')

class td(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('td', attr=attr, content=content, tag_type='double')

