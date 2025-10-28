import array

arr = array.array('i', [10, 20, 30, 40, 50])

for index, element in enumerate(arr):
    print(f"arr[{index}] = {element}")