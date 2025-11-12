ch = 'a'
print(f"Original Character = \'{ch}\'")

if ch.isupper():
    print(f"Character: \'{ch}\' is an uppercase character.")
elif ch.islower():
    print(f"Character: \'{ch}\' is a lowercase character.")
else:
    print(f"Case of Character: \'{ch}\' could not be determined.")