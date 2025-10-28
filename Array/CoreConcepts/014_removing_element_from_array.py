import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original Array, arr = {arr}")

del arr[0]
print(f"After removing an element from the beginning of the array, arr = {arr}")

del arr[-1]
print(f"After removing an element from the end of the array, arr = {arr}")

del arr[1]
print(f"After removing an element from the first index of the array, arr = {arr}")
