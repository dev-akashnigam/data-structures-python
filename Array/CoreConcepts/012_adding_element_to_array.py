import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original Array, arr = {arr}")

arr.insert(0, 5)
print(f"After inserting element: 5 at the beginning of the array, arr = {arr}")

arr.insert(len(arr), 100)
print(f"After inserting element: 100 at the end of the array, arr = {arr}")

arr.insert(4, 35)
print(f"After inserting element: 35 at the forth index of the array, arr = {arr}")