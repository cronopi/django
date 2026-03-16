import sys

def parse_elements():
	elements = {}

	with open("periodic_table.txt", 'r') as file:
		for line in file:
			temp = line.split(' = ')
			name = temp[0]
			values = temp[1].strip()



	print(elements.keys())
	#print(elements.values())


if __name__ == "__main__":
	parse_elements()
