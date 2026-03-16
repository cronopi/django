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
	print(states_inverted)

	if capital in capital_cities.values():
		print("lo encontré")

def main():
	capital_city(sys.argv[1])
