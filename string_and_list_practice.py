## 1) Find and replace:
# In this string: str = "It's thanksgiving day. It's my birthday,too!" print the position of the 
# first instance of the word "day". Then create a new string where the word "day" is 
# replaced with the word "month".

def find_and_replace(str):
	position = str.find("day")
	print position
	second_str = str.replace("day", "month", 1)
	print second_str

find_and_replace("It's thanksgiving day. It's my birthday,too!")

# str.replace(old, new[, max])