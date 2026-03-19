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
	"""Generate HTML table from 2D array"""
	html = '<table>\n'

	# Iterate through each row
	for row in table:
		html += '<tr>\n'

		# Iterate through each cell in row
		for cell in row:
			if cell is None:
				# Empty cell
				html += '<td></td>\n'
			else:
				# Cell with element
				element_name = cell
				element_data = elements[element_name]
				html += generate_cell_html(element_name, element_data)

		html += '</tr>\n'

	html += '</table>\n'
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

	# Generate the full table HTML
	table_html = generate_table_html(table_complete, elements)

	# Print first 500 characters to see structure
	print(table_html[:500])
	print("\n...\n")


