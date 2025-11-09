str = "When the rain stopped, the city lights looked brighter than ever"
print(f"Original String = {str}")

subs = "brighter"

has_check = subs in str

print(f"String: \"{str}\" has substring \"{subs}\" = {has_check}")