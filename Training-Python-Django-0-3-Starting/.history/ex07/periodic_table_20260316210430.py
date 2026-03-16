import sys

def create_table():
	table = []

	for row in range(7):
		row = []
		for column in range(18):
			row.append(None)
		table.append(row)

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
