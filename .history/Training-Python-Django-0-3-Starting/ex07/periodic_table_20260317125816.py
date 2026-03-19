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


	hydrogen_data = elements['Hydrogen']
	cell_html = generate_cell_html('Hydrogen', hydrogen_data)
	print(cell_html)
	print("\n---\n")

	empty_table = create_table()
	table_complete = fill_table(empty_table, elements)


