import array

arr = array.array('i', [10, 50, 30, 20, 40])
print(f"Original array, arr = {arr}")

search_element = 20

if search_element in arr:
    print(f"Element: {search_element} is present in the array.")

    first_index = arr.index(search_element)
    print(f"First index of search element: {search_element} = {first_index}")

    # there exists no built-in method in PY that helps in determining the index of the last matching element.
else:
    print(f"Element: {search_element} is NOT present in the array.")