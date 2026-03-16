import sys

def capital_city(capital):
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

	# Invertir los diccionarios para buscar por valor
	capital_cities_inv = {valor: clave for clave, valor in capital_cities.items()}
	states_inv = {valor: clave for clave, valor in states.items()}

	# Buscar: capital → código → estado
	if capital in capital_cities_inv:
		code = capital_cities_inv[capital]
		state = states_inv[code]
		print(state)
	else:
		print("Unknown capital city")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit(1)
	capital_city(sys.argv[1])
