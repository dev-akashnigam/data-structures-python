ch = 'w'
print(f"Original Character = {ch}")

ch_is_alphabet = ch.isalpha()
ch_is_digit = ch.isdigit()
ch_is_whitespace = ch.isspace()

if ch_is_alphabet:
    print(f"Character: {ch} is a letter/alphabet.")
elif ch_is_digit:
    print(f"Character: {ch} is a digit.")
elif ch_is_whitespace:
    print(f"Character: {ch} is a whitespace.")
else:
    print(f"Character: {ch} is a special character.")


