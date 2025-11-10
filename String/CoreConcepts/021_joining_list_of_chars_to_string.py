# In PY, there is no difference between a character and a string.
# Infact, characters are strings of length = 1.
# Therefore, joining a list of strings or list of characters is one and the same thing in PY.

char_list = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
print(f"List of characters = {char_list}")

joined_str = "".join(char_list)
print(f"String formed after joining list of characters = {joined_str}")