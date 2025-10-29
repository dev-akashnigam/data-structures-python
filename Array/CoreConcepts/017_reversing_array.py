import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original Array, arr = {arr}")

arr.reverse()
print(f"Reversed Array, arr = {arr}")
