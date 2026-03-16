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
		print(f"{capital_cities[code]} is the capital of {state}")
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
		print(f"{capital} is the capital of {states_inverted[code]}")
	else:
		print("Unknown capital")


def print_capital_and_state(items):
	states, capital_cities = get_dictionaries()

	for state in states:
			if state.lower() == items_lower:
				state_to_capital(state)
				return

	for capital in capital_cities.values():
		if capital.lower() == items_lower:
			capital_to_state(capital)
			return
	else:
		print(f"{items} is neither a capital city nor a state")

def parser(arguments):
	items = arguments.split(",")
	for item in items:
		item = item.strip()
		if item:
			print_capital_and_state(item)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit(1)

	parser(sys.argv[1])
