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
	states_inverted = {}
	for state, code in states.items():
		states_inverted[code] = state
	capital_cities_inverted = {}
	for code, city in capital_cities.items():
		capital_cities_inverted[city] = code

	if valor in capital_cities_inverted:
		code = capital_cities_inverted[valor]
		print(states_inverted[code])



if __name__ == "__main__":
	capital_city(sys.argv[1])
