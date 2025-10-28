import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original Array, arr = {arr}")

arr = array.array('i',[3, 6, 9]) + arr
print(f"After inserting elements: 3, 6, 9 at the beginning of the array, arr = {arr}")

arr = arr + array.array('i',[300, 600, 900])
print(f"After inserting elements: 300, 600, 900 at the end of the array, arr = {arr}")

arr[6:6] = array.array('i',[33, 36, 39])
print(f"After inserting elements: 33, 36, 39 at the sixth index of the array, arr = {arr}")