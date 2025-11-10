# In Python, strings are immutable — you cannot modify them in place. Therefore, there’s no method like insert() for strings.
str = "Although it was raining, they continued the game"
print(f"Original String = {str}")

insertion_text = "paining and "
insertion_index = 16

strOnInsertion = str[:16] + insertion_text + str[16:]
print(f"After inserting text: \"{insertion_text}\" at index: {insertion_index}, string = \"{strOnInsertion}\"")