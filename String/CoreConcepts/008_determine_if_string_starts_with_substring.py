str = "The curious fox wandered through the misty valley at dawn"
print(f"Original String = {str}")

subs = "The"

start_check = str.startswith(subs)

print(f"String: \"{str}\" starts with substring: \"{subs}\" is = {start_check}")