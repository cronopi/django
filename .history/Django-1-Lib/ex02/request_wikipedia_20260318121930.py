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

if __name__ == "__main__":
	main()
