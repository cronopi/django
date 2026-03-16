import sys

def parse_elements():
	elements = {}

	with open("periodic_table.txt", 'r') as file:
		for line in file:
			elements.name = line.split('=')[0]


if __name__ == "__main__":
	parse_elements()
