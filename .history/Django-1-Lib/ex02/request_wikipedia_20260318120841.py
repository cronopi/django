import sys
import requests
import json

def main():
	if len(sys.argv) != 2:
		print("Usage: python request_wikipedia.py <search_term>")
		return

	words_to_search = " ".join(sys.argv[1:])


if __name__ == "__main__":
	main()
