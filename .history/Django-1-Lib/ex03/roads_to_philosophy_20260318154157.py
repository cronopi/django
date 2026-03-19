import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 roads_to_philosophy.py <search_term>")
        sys.exit(1)

    search_term = " ".join(sys.argv[1:])

if __name__ == "__main__":
    main()
