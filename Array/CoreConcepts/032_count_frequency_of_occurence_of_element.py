import array

arr = array.array('i', [10, 20, 30, 40, 50, 20, 40, 60, 40, 50, 40, 60])
print(f"Original array, arr = {arr}")

element = 40
frequency_of_element = arr.count(element)

print(f"Frequency or count of occurence of element: {element} = {frequency_of_element}")
