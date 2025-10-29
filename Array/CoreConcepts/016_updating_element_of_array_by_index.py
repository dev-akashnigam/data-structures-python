import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original Array, arr = {arr}")

arr[0] = 100
print(f"Array after updating the first array element with value: 100, arr = {arr}")

arr[-1] = 500
print(f"Array after updating the last array element with value: 500, arr = {arr}")

arr[2] = 300
print(f"Array after updating the array element at index: 2 with value: 300, arr = {arr}")
