from stats import *

def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	chars_dict = get_char_dict(text)
	list_dicts = []
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
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
