from elem import Elem, Text


class Html(Elem):
	def __init__(self, content=None, **attr):
		super().__init__('html', attr=attr, content=content, tag_type='double')


