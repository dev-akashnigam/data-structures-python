import array

arr = array.array('i', [10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50])

search_element = 30

if search_element in arr:
    print(f"Element: {search_element} is PRESENT in the array.")

    element_first_index = arr.index(search_element)
    print(f"Element: {search_element} PRESENT at index = {element_first_index}")

    # built-in function to determine the last index of the search element is not available in Python.
else:
    print(f"Element: {search_element} is NOT PRESENT in the array.")

