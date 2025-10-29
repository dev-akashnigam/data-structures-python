import array

arr = array.array('i', [30, 50, 40, 10, 20])
print(f"Original Array, arr = {arr}")

arr = array.array('i', sorted(arr))
print(f"Sorted Array in Ascending Order, arr = {arr}")