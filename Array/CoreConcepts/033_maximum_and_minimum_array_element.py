import array

arr = array.array('i', [40, 30, 50, 60, 20, 10, 70, 90, 80])
print(f"Original Array, arr = {arr}")

max_element = max(arr)
min_element = min(arr)

print(f"Max element = {max_element}, Min element = {min_element}")