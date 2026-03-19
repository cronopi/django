class Text(str):
	"""Represents HTML text content with proper escaping."""
	
	def __new__(cls, content=''):
		# Convert to string if needed
		content = str(content)
		
		# Escape HTML special characters
		content = content.replace('&', '&amp;')
		content = content.replace('<', '&lt;')
		content = content.replace('>', '&gt;')
		content = content.replace('"', '&quot;')
		
		# Create string instance
		return str.__new__(cls, content)


class Elem:
	"""Base class for all HTML elements."""
	
	def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
		"""
		Initialize an HTML element.
		
		Args:
			tag: HTML tag name (e.g., 'div', 'table', 'p')
			attr: Dictionary of attributes (e.g., {'class': 'myclass'})
			content: Single content item or list of items (Elem or Text)
			tag_type: 'double' for <tag>...</tag> or 'simple' for <tag />
		"""
		self.tag = tag
		self.attr = attr or {}
		self.tag_type = tag_type
		self.content = []
		
		if content is not None:
			self.add_content(content)
	
	def add_content(self, content):
		"""Add content to element."""
		if isinstance(content, list):
			for item in content:
				if isinstance(item, (Text, Elem)):
					if isinstance(item, Text) and str(item) == '':
						continue
					self.content.append(item)
		elif isinstance(content, (Text, Elem)):
			if isinstance(content, Text) and str(content) == '':
				return
			self.content.append(content)
	
	def __str__(self):
		"""Generate HTML string representation."""
		# Build attributes string
		attr_str = ''
		for key, value in self.attr.items():
			attr_str += f' {key}="{value}"'
		
		# Self-closing tags
		if self.tag_type == 'simple':
			return f'<{self.tag}{attr_str} />'
		
		# Empty tags
		if not self.content:
			return f'<{self.tag}{attr_str}></{self.tag}>'
		
		# Tags with content - indent for readability
		content_lines = []
		for item in self.content:
			item_str = str(item)
			for line in item_str.split('\n'):
				content_lines.append('  ' + line)
		
		content_str = '\n' + '\n'.join(content_lines) + '\n'
		return f'<{self.tag}{attr_str}>{content_str}</{self.tag}>'
