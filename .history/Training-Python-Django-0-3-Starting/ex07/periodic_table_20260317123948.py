import sys

def get_row(number):
	if number <= 2:
		return 0
	elif number <= 10:
		return 1
	elif number <= 18:
		return 2
	elif number <= 36:
		return 3
	elif number <= 54:
		return 4
	elif number <= 86:
		return 5
	else:
		return 6

def fill_table(table, elements):

	for name in elements:
		number = int(elements[name]['number'])
		position = int(elements[name]['position'])

		fila = get_row(number)
		columna = int(position)

		table[fila][columna] = name
	return table


def create_table():
	table = []

	table = [[None] * 18 for _ in range(7)]
	print(len(table))
	print(len(table[0]))
	return table

def parse_elements():
	elements = {}

	with open("periodic_table.txt", 'r') as file:
		for line in file:
			name = line.split(' = ')[0].strip()
			temp_values = line.split(' = ')[1].strip()

			temp_values_splited = temp_values.split(', ')
			attributes = {}

			for temp in temp_values_splited:
				key = temp.split(':')[0].strip()
				value = temp.split(':')[1].strip()
				attributes[key] = value

			elements[name] = attributes

	return elements

def generate_html(table, elements):
	"""Generate HTML code for the periodic table."""
	html = '<!DOCTYPE html>\n'
	html += '<html>\n'
	html += '<head>\n'
	html += '<meta charset="utf-8">\n'
	html += '<title>Periodic Table of Elements</title>\n'
	html += '<style>\n'
	html += 'table { border-collapse: collapse; margin: 20px; }\n'
	html += 'td { border: 1px solid black; padding: 10px; width: 60px; height: 60px; text-align: center; }\n'
	html += 'h4 { margin: 5px 0; font-size: 12px; }\n'
	html += 'ul { margin: 5px 0; padding-left: 15px; font-size: 10px; }\n'
	html += 'li { margin: 2px 0; }\n'
	html += '</style>\n'
	html += '</head>\n'
	html += '<body>\n'
	html += '<h1>Periodic Table of Elements</h1>\n'
	html += '<table>\n'
	
	# Generate each row
	for row in table:
		html += '<tr>\n'
		for cell in row:
			if cell is None:
				# Empty cell
				html += '<td></td>\n'
			else:
				# Cell with element
				element_name = cell
				element_data = elements[element_name]
				html += '<td>\n'
				html += f'<h4>{element_name}</h4>\n'
				html += '<ul>\n'
				html += f'<li>No {element_data["number"]}</li>\n'
				html += f'<li>{element_data["small"]}</li>\n'
				html += f'<li>{element_data["molar"]}</li>\n'
				html += f'<li>{element_data["electron"]} electrons</li>\n'
				html += '</ul>\n'
				html += '</td>\n'
		html += '</tr>\n'
	
	html += '</table>\n'
	html += '</body>\n'
	html += '</html>\n'
	
	return html


def write_html_file(html_content, filename):
	"""Write HTML content to a file."""
	try:
		with open(filename, 'w', encoding='utf-8') as f:
			f.write(html_content)
		print(f"File '{filename}' written successfully!")
	except IOError as e:
		print(f"Error writing file: {e}")


if __name__ == "__main__":
	elements = parse_elements()
	table = create_table()
	table = fill_table(table, elements)
	
	# Generate HTML
	html_content = generate_html(table, elements)
	
	# Write to file
	write_html_file(html_content, "periodic_table.html")
