import sys

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
		print(capital_cities[code])
		print(f"{states[1]}")

	else:
		print("Unknown state")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		sys.exit(1)
	capital_city(sys.argv[1])
