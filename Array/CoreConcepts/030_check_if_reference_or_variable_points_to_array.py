import array

arr1 = array.array('i', [10, 20, 30, 40, 50])
print(f"Variable arr = {arr1}")

arr2 = 10
print(f"Variable arr2 = {arr2}")

print(f"Is variable arr1 an array = {isinstance(arr1, array.array)}")
print(f"Is variable arr2 an array = {isinstance(arr2, array.array)}")
