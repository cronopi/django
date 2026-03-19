import sys

def generate_cell_html(element_name, element_data):

	html = '<td>\n'
	html += f'<h4>{element_name}</h4>\n'
	html += '<ul>\n'
	html += f'<li>No {element_data["number"]}</li>\n'
	html += f'<li>{element_data["small"]}</li>\n'
	html += f'<li>{element_data["molar"]}</li>\n'
	html += f'<li>{element_data["electron"]} electrons</li>\n'
	html += '</ul>\n'
	html += '</td>\n'
	return html

def generate_table_html(table, elements):
	html = '<table>\n'

	for row in table:
		html += '<tr>\n'

		for cell in row:
			if cell is None:
				# Empty cell
				html += '<td></td>\n'
			else:
				element_name = cell
				element_data = elements[element_name]
				html += generate_cell_html(element_name, element_data)

		html += '</tr>\n'

	html += '</table>\n'
	return html

def generate_complete_html(table, elements):

	html = '<!DOCTYPE html>\n'
	html += '<html>\n'
	html += '<head>\n'
	html += '<meta charset="utf-8">\n'
	html += '<title>Periodic Table of Elements</title>\n'
	html += '<style>\n'
	html += 'body { font-family: Arial, sans-serif; margin: 20px; }\n'
	html += 'table { border-collapse: collapse; margin: 20px; }\n'
	html += 'td { border: 1px solid black; padding: 10px; text-align: center; min-width: 80px; }\n'
	html += 'h4 { margin: 5px 0; font-size: 14px; }\n'
	html += 'ul { margin: 5px 0; padding-left: 15px; font-size: 11px; list-style: none; }\n'
	html += 'li { margin: 2px 0; }\n'
	html += '</style>\n'
	html += '</head>\n'
	html += '<body>\n'
	html += '<h1>Periodic Table of Elements</h1>\n'

	# Add the table
	html += generate_table_html(table, elements)

	html += '</body>\n'
	html += '</html>\n'
	return html

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
	#print(len(table))
	#print(len(table[0]))
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

if __name__ == "__main__":
	elements = parse_elements()
	empty_table = create_table()
	table_complete = fill_table(empty_table, elements)

	# Generate complete HTML document
	complete_html = generate_complete_html(table_complete, elements)

	# Write to file
	try:
		with open("periodic_table.html", "w", encoding="utf-8") as f:
			f.write(complete_html)
		print("✓ File 'periodic_table.html' created successfully!")
	except IOError as e:
		print(f"✗ Error writing file: {e}")


