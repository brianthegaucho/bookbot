def get_num_words(text):
	words = text.split()
	return len(words)


def sort_on(items):
	return items["num"]


def get_char_dict(text):
	chars = {}
	for c in text:
		lowered = c.lower()
		if lowered in chars:
			chars[lowered] += 1
		else:
			chars[lowered] = 1
	return chars
