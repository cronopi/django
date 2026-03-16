import sys

def fill_table(table, elements):

	for name, data in elements.items():
		fila = get_fila(int(data['number']))
        columna = int(data['position'])

        # Pones el elemento en su lugar
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

if __name__ == "__main__":
	elements = parse_elements()
	table = create_table()
