def var_to_dict(dictionary):
	result = {}
	for name, year in dictionary:
		if year not in result:
			result[year] = []
			print(f"Creating new entry for year {year}")

if __name__ == "__main__":
	dictionary = [
		('Hendrix', '1942'),
		('Garcia', '1942'),
		('Page', '1944'),
		('Beck', '1944'),
		('Johnson', '1911'),
	]
	var_to_dict(dictionary)
