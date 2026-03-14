
class Text(str):
	def __new__(cls, content=''):

		content = str(content)

		content = content.replace('&', '&amp;')
		content = content.replace('<', '&lt;')
		content = content.replace('>', '&gt;')
		content = content.replace('"', '&quot;')


		content = content.replace('\n', '\n<br />\n')


		return str.__new__(cls, content)


class Elem:
	def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
		self.tag = tag
		self.attr = attr or {}
		self.tag_type = tag_type
		self.content = []

	class ValidationError(Exception):
		pass

	def __str__(self):
		attr_str = ''
		for key, value in self.attr.items():
			attr_str += f' {key}="{value}"'

		if self.tag_type == 'simple':
			return f'<{self.tag}{attr_str} />'

		if not self.content:
			return f'<{self.tag}{attr_str}></{self.tag}>'

		content_lines = []
		for item in self.content:
			item_str = str(item)
			for line in item_str.split('\n'):
				content_lines.append('  ' + line)

		content_str = '\n' + '\n'.join(content_lines) + '\n'
		return f'<{self.tag}{attr_str}>{content_str}</{self.tag}>'

	def add_content(self):
