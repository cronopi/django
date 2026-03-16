import sys

def parse_elements():
	elements = {}

	with open("periodic_table.txt", 'r') as file:
		for line in file:
			elements[line.split('=')[0]] = line.split('=')[1]

	attributes_str = 'position:0, number:1, small: H, molar:1.00794, electron:1'

	attributes = attributes_str.split(', ')
	print(attributes)


if __name__ == "__main__":
	parse_elements()
