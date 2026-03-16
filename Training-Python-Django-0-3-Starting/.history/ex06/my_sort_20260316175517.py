
def dictionary():
	d = {
		'Zoe' : '2000',
		'Alice' : '2000',
		'Bob' : '2000',
		'Charlie' : '1995',
		'David' : '1990',
		'Eve' : '1990',
		'Frank' : '1985',
	}
	return d

def display_musicians_sorted_by_year(d):
	d = dict(sorted(d.items()))
	d_inverted = {}
	for name, year in d.items():
		if year not in d_inverted:
			d_inverted[year] = []
		d_inverted[year].append(name)
	d_inverted_sorted = sorted(d_inverted.items())

	for year, names in d_inverted_sorted:
		for name in names:
			print(f"{name}")

if __name__ == "__main__":
	d = dictionary()
	display_musicians_sorted_by_year(d)
