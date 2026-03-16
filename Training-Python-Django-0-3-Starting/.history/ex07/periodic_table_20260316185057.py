import sys

def parse_elements():
	elements = {}

	file = open("periodic_table.txt", 'r')
	for line in file:
		print(line)
	file.close()
if __name__ == "__main__":
	parse_elements()
