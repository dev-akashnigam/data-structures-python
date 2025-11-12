str_1 = "Life moves fast"
print(f"First string = {str_1}")

str_2 = "LIFE MOVES FAST"
print(f"Second string = {str_2}")

are_text_same = str_1.lower() == str_2.lower()

if are_text_same:
    print(f"Both the strings have same text.")
else:
    print(f"Both the strings have different text.")