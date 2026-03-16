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
	
	# Invertir capital_cities de forma explícita
	capital_cities_inv = {}
	for code, city in capital_cities.items():
		capital_cities_inv[city] = code
	
	# Invertir states de forma explícita
	states_inv = {}
	for state, code in states.items():
		states_inv[code] = state
	
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
