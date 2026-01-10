def get_book_text(path):
	with open(path) as f:
		return f.read()

def sort_on(items):
	return items[0]

def get_char_dict(text):
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	chars = {}
	for c in text:
		lowered = c.lower()
		if lowered in chars:
			chars[lowered] += 1
		else:
			chars[lowered] = 1
	print(chars(sorted(key=sort_on, reverse=True)))

get_char_dict("books/frankenstein.txt")