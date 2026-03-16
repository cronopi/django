import sys

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
