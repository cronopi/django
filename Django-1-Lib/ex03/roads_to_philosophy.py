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

		visited = []
		current_url = response.url

		while True:
			# Extraer título del artículo
			if "/wiki/" not in current_url:
				print("It's a dead end !")
				break

			article_title = current_url.split("/wiki/")[1]

			visited.append(article_title)
			print(article_title)

			if article_title == "Philosophy":
				print(f"{len(visited)} roads from {search_term} to philosophy !")
				break

			response = requests.get(current_url, headers=headers)
			html_content = response.text

			content = BeautifulSoup(html_content, "html.parser")
			main_content = content.find('div', id='mw-content-text')

			if not main_content:
				print("It's a dead end !")
				break

			paragraphs = main_content.find_all('p')

			first_link = None
			for para in paragraphs:
				for link in para.find_all('a'):
					if link.get('href', '').startswith('/wiki/'):
						first_link = link
						break

				if first_link:
					break

			if not first_link:
				print("It's a dead end !")
				break

			current_url = "https://en.wikipedia.org" + first_link['href']

	except Exception as e:
		print(f"Error: {e}")
		sys.exit(1)

if __name__ == "__main__":
	main()
