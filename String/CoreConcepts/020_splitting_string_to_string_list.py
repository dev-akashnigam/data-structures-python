# In PY, there is no difference between a character and a string.
# Infact, characters are strings of length = 1.
# Therefore, splitting a string into array of strings or array of characters is one and the same thing in PY.

str = "The sun is bright"
print(f"Original String = {str}")

list_of_chars_or_strings = list(str)
print(f"List of Chars or Strings = {list_of_chars_or_strings}")