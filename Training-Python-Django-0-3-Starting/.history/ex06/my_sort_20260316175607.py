
def dictionary():
	d = {
		'Zara' : '2005',
		'Yuki' : '2005',
		'Xander' : '2005',
		'Walter' : '2000',
		'Victor' : '2000',
		'Uma' : '1995',
		'Tom' : '1990',
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
