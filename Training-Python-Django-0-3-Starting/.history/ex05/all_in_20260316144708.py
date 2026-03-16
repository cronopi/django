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

def capital_city(state):
	states, capital_cities = get_dictionaries()

	if state in states:
		code = states[state]
		print(capital_cities[code])
	else:
		print("Unknown state")

def capital_city(capital):
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


def dictionary():
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

	print("States:")
	for state in states:
		print(state)
	print("\nCapital Cities:")
	for city in capital_cities.values():
		print(city)


if __name__ == "__main__":

	dictionary()
