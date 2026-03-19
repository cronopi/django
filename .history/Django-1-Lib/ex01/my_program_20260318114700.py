
from path import Path

def main():
	my_folder = Path("my_folder")
	my_folder.mkdir_p()

	my_file = my_folder/"my_file.txt"
	my_file.write_text("Hello, World!")

	print(my_file.read_text())

if __name__ == "__main__":
	main()
