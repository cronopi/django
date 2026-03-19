import sys
import requests
import json

def main():
	if len(sys.argv) != 2:
		print("Usage: python request_wikipedia.py <search_term>")
		return

	words_to_search = " ".join(sys.argv[1:])
	url = "https://en.wikipedia.org/w/api.php"
	instructions = {
	"action": "query",
	"format": "json",
	"titles": words_to_search,
	"prop": "extracts",
	"explaintext": True
}
	try:
		response = requests.get(url, params=instructions)
		print(response.status_code)
""" 		filename = words_to_search.replace(" ", "_") + ".wiki"
		with open(filename, 'w', encoding='utf-8') as file:
		file.write(content)

		print(f"Archivo '{filename}' creado exitosamente") """
	except Exception as e:
		print(f"An error occurred: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()
