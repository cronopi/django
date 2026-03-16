def var_to_dict(dictionary):
	result = {}
	for name, year in dictionary:
		if year not in result:
			result[year] = []
		result[year].append(name)
	print(f"{result}")
	""" for year, name in result.items():
		print(f"{year} : {' '.join(name)}") """


if __name__ == "__main__":
	dictionary = [
		('Hendrix', '1942'),
		('Garcia', '1942'),
		('Page', '1944'),
		('Beck', '1944'),
		('Johnson', '1911'),
	]
	var_to_dict(dictionary)
