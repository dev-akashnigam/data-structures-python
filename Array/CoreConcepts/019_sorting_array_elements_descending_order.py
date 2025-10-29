import array

arr = array.array('i', [30, 50, 40, 10, 20])
print(f"Original Array, arr = {arr}")

arr = array.array('i', sorted(arr, reverse=True))
print(f"Sorted Array in Descending Order, arr = {arr}")