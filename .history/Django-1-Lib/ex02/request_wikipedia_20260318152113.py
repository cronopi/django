import sys
import requests
import json

def main():
	if len(sys.argv) < 2:
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
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
	}
	try:
		response = requests.get(url, params=instructions, headers=headers)
		data = response.json()
		data = data["query"]["pages"]
		
		if not data:
			print("Error: article not found")
			sys.exit(1)
		
		page_id = list(data.keys())[0]
		
		if 'extract' not in data[page_id]:
			print("Error: article has no content")
			sys.exit(1)
		
		content = data[page_id]["extract"]

		filename = words_to_search.replace(" ", "_") + ".wiki"
		with open(filename, "w", encoding="utf-8") as file:
			file.write(content)

	except Exception as e:
		print(f"Error: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()
