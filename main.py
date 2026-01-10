import sys
from stats import *

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		book_path = str(sys.argv[1])
		text = get_book_text(book_path)
		num_words = get_num_words(text)
		chars_dict = get_char_dict(text)
		list_dicts = []
		print("============ BOOKBOT ============")
		print("Analyzing book found at", sys.argv[1],"...")
		print("----------- Word Count ----------")
		print("Found",num_words,"total words")
		print("--------- Character Count -------")
		for char in chars_dict:
			list_dicts.append({"char": char, "num": chars_dict[char]})
		list_dicts.sort(reverse=True, key=sort_on)
		for item in list_dicts:
			ch = item["char"]
			count = item["num"]
			if ch.isalpha():
				print(f"{ch}: {count}")


def get_book_text(path):
	with open(path) as f:
		return f.read()


main()
