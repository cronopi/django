import sys

def parse_elements():
	elements = {}


	with open("periodic_table.txt", 'r') as file:
		for line in file:
			name = line.split(' = ')[0]
			temp_values = line.split(' = ')[1]

			temp_values_splited = temp_values.split(', ')
			attributes = {}

			for temp in temp_values_splited:
				key = temp.split(':')[0]
				value = temp.split(':')[1]
				attributes[key] = value

			elements[name] = attributes

	return elements

if __name__ == "__main__":
	parse_elements()
