import sys

def parse_elements():
	elements = {}

	with open("periodic_table.txt", 'r') as file:
		for line in file:
			temp = line.split(' = ')


	elements.values() = elements.values().split(', ')
	#print(elements.values())
	print(elements.keys())


if __name__ == "__main__":
	parse_elements()
