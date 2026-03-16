import sys

# PASO 1: Copiar los diccionarios
states = {
    "Oregon": "OR",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado": "CO"
}

capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def capital_city(state):
	if state in states:
		code = states[state]
	if code is Empty:
		print("Unknown state")
	else:
		print(capital_cities[code])

	return None

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit(1)
	capital_city(sys.argv[1])
