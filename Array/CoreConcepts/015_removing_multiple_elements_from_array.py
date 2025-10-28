import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original Array, arr = {arr}")

del arr[0:2] # or del arr[:2]
print(f"After removing 2 elements from the beginning of the array, arr = {arr}")

del arr[-2:len(arr)] # or del arr[-2:]
print(f"After removing 2 elements from the end of the array, arr = {arr}")

del arr[0:1]
print(f"After removing 1 element from the only index(0) of the array, arr = {arr}")
