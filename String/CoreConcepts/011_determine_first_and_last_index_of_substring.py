str = "They laughed and laughed until they cried"
print(f"Original String = {str}")

subs = "laughed"

has_check = subs in str
print(f"String: \"{str}\" has substring \"{subs}\" = {has_check}")

if has_check:
    first_index = str.find(subs)
    last_index = str.rfind(subs)

    print(f"First index of substring: \"{subs}\" = {first_index}")
    print(f"Last index of substring: \"{subs}\" = {last_index}")