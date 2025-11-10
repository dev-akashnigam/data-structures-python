# In PY, there is no difference between a character and a string.
# Infact, characters are strings of length = 1.
# Therefore, joining a list of strings or list of characters is one and the same thing in PY.

string_list = ["You", "look", "nice"]
print(f"List of strings = {string_list}")

joined_str = " ".join(string_list)
print(f"String formed after joining list of strings = {joined_str}")