import sys

def geohash(latitude, longitude):
	lon_min = -180.0
	lon_max = 180.0
	lat_min = -90.0
	lat_max = 90.0

	bits = ""

	for i in range(10):
		if i % 2 == 0:
			lon_middle = (lon_min + lon_max) / 2
			if longitude >= lon_middle:
				bits += "1"
				lon_min = lon_middle
			else:
				bits += "0"
				lon_max = lon_middle

		else:
			lat_middle = (lat_min + lat_max) / 2
			if latitude >= lat_middle:
				bits += "1"
				lat_min = lat_middle
			else:
				bits += "0"
				lat_max = lat_middle

	base32 = "0123456789bcdefghjkmnpqrstuvwxyz"

	temp = bits[0:5]
	number1 = int(temp, 2)
	caracter1 = base32[number1]

	temp = bits[5:10]
	number2 = int(temp, 2)
	caracter2 = base32[number2]


	geohash = caracter1 + caracter2

	return geohash

def validate_coordinates(latitude, longitude):
	if latitude < -90 or latitude > 90:
		print("Invalid latitude. It must be between -90 and 90.")
		sys.exit(1)
	if longitude < -180 or longitude > 180:
		print("Invalid longitude. It must be between -180 and 180.")
		sys.exit(1)

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("please use this prompt: python geohashing.py <latitude> <longitude>")
		sys.exit(1)

	try:
		latitude = float(sys.argv[1])
		longitude = float(sys.argv[2])
	except ValueError:
		print("Error: Latitude and longitude must be valid numbers.")
		sys.exit(1)

	validate_coordinates(latitude, longitude)

	result = geohash(latitude, longitude)
	print(result)
