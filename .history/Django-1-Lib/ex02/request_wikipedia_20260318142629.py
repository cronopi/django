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
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
	}
	try:
		response = requests.get(url, params=instructions, headers=headers)
		data = response.json()
		data = data["query"]["pages"]
		page_id = list(data.keys())[0]
		print(page_id)
		content = data[page_id]["extract"]
		print(content)

	except Exception as e:
		print(f"An error occurred: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()
