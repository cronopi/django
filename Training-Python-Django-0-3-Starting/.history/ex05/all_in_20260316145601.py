import sys

def get_dictionaries():
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

    return states, capital_cities

def state_to_capital(state):
	states, capital_cities = get_dictionaries()

	if state in states:
		code = states[state]
		print(capital_cities[code])
	else:
		print("Unknown state")

def capital_to_state(capital):
	states, capital_cities = get_dictionaries()

	states_inverted = {}
	for state, code in states.items():
		states_inverted[code] = state
	capital_cities_inverted = {}
	for code, city in capital_cities.items():
		capital_cities_inverted[city] = code

	if capital in capital_cities_inverted:
		code = capital_cities_inverted[capital]
		print(states_inverted[code])
	else:
		print("Unknown capital")


def print_all():


	return None


if __name__ == "__main__":
	print_all(sys.argv[1])
