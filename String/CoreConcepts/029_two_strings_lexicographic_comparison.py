'''
Lexicographic comparison is how strings (or sequences of characters) are compared based on dictionary order — i.e., 
the same way words are ordered in a dictionary.

So when strings like "apple" and "banana" are compared lexicographically,
the characters of both strings are compared one by one, using their Unicode (ASCII) values to decide which comes first.
'''

str_1 = "apple"
print(f"First String = {str_1}")

str_2 = "banana"
print(f"Second String = {str_2}")

result = str_1 < str_2

if result:
    print(f"{str_1} < {str_2}")
else:
    print(f"{str_1} >= {str_2}")