
def dictionary():
	d = {
		'Hendrix' : '1942',
		'Allman' : '1946',
		'King': '1925',
		'Clapton' : '1945',
		'Johnson' : '1911',
		'Berry': '1926',
		'Vaughan' : '1954',
		'Cooder' : '1947',
		'Page': '1944',
		'Richards' : '1943',
		'Hammett' : '1962',
		'Cobain' : '1967',
		'Garcia' : '1942',
		'Beck' : '1944',
		'Blackmore' : '1944',
		'Santana' : '1947',
		'Ramone' : '1948',
		'White': '1975',
		'Frusciante': '1970',
		'Thompson' : '1949',
		'Burton' : '1939',
	}
	return d

def display_musicians_sorted_by_year(d):
	d = dict(sorted(d.items()))
	#print(d)
	d_inverted = {}
	for name, year in d.items():
		d_inverted[year] = name
	d_inverted_sorted = dict(sorted(d_inverted.items()))
	#print(d_inverted_sorted)
	for year, name in d_inverted_sorted.items():
		print(f"{name}" f" was born in {year}")

if __name__ == "__main__":
	d = dictionary()
	display_musicians_sorted_by_year(d)
