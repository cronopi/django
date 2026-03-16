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

if __name__ == "__main__":
	elements = parse_elements()
	table = create_table()
	table = fill_table(table, elements)

	 # TEST 1: Fila 0
    print("Fila 0, Columna 0:", table[0][0])   # Debería: Hydrogen
    print("Fila 0, Columna 17:", table[0][17])  # Debería: Helium

    # TEST 2: Fila 1
    print("Fila 1, Columna 0:", table[1][0])   # Debería: Lithium
    print("Fila 1, Columna 1:", table[1][1])   # Debería: Beryllium
    print("Fila 1, Columna 12:", table[1][12]) # Debería: Boron
    print("Fila 1, Columna 17:", table[1][17]) # Debería: Neon

    # TEST 3: Fila 2
    print("Fila 2, Columna 0:", table[2][0])   # Debería: Sodium
    print("Fila 2, Columna 17:", table[2][17]) # Debería: Argon

    # TEST 4: Espacios vacíos
    print("Fila 0, Columna 1:", table[0][1])   # Debería: None (vacío)
    print("Fila 1, Columna 2:", table[1][2])   # Debería: None (vacío)
