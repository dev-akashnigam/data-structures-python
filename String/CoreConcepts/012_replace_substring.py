str = "The mountain stood unmoved, watching centuries pass below"
print(f"Original String = {str}")

substringToReplace = "watching"
newSubstring = "gazing"

str = str.replace(substringToReplace, newSubstring)
print(f"After replacing substring: \"{substringToReplace}\" with \"{newSubstring}\", the string becomes = \"{str}\"")