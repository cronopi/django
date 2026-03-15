#!/usr/bin/env python3

def read_and_display_numbers(filename):
    try:
        file = open("numbers.txt", "r")
        file_numbers = file.read()
        numbers_splited = file_numbers.replace(',', '\n')
        print(numbers_splited, end='')
        file.close()
    except FileNotFoundError:
        print(f"Error: can't find the file {filename}")

if __name__ == "__main__":
    read_and_display_numbers("numbers.txt")
