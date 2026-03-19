from elem import Elem

class Page:
	"""Class to manage HTML pages and write them to files."""
	
	def __init__(self, elem):
		"""
		Initialize Page with an Elem instance.
		
		Args:
			elem: Root element (typically Html)
		"""
		if not isinstance(elem, Elem):
			raise ValueError("Page must be initialized with an Elem instance")
		self.elem = elem
	
	def __str__(self):
		"""Return HTML string with doctype if root is Html."""
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
			print(f"File '{filename}' written successfully")
		except IOError as e:
			raise IOError(f"Failed to write to file {filename}: {e}")
