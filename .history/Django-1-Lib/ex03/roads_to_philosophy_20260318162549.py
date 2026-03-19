import sys
import requests
from bs4 import BeautifulSoup

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 roads_to_philosophy.py <search_term>")
		sys.exit(1)

	search_term = " ".join(sys.argv[1:])

	url = f"https://en.wikipedia.org/w/index.php?title=Special:Search&search={search_term}"
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
	}

	try:
		response = requests.get(url, headers=headers)
		html = response.text
		print(html)
	except Exception as e:
		print(f"Error: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()
