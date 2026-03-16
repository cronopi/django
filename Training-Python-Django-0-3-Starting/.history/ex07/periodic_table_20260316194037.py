import sys

def parse_elements():
	elements = {}

	with open("periodic_table.txt", 'r') as file:
		for line in file:
			temp = line.split(' = ')
			name = temp[0]
			temp_values = temp[1].strip()

			temp_values_splited = temp_values.split(', ')

			attributes = {}
			for temp in temp_values_splited:
				key, value = temp.split(': ')
				attributes[key] = value

			elements[name] = attributes

	print(elements.keys())
	print(elements.values())


if __name__ == "__main__":
	parse_elements()
