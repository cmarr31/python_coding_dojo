def find_characters(lst, str):
	items = [y for y in lst if str in y]
	print items

find_characters(["cat", "attack", "dog", "pat"], "t")