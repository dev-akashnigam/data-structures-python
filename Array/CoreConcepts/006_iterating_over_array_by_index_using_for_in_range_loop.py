import array

arr = array.array('i', [10, 20, 30, 40, 50])

for index in range(0, len(arr), 1):
    print(f"arr[{index}] = {arr[index]}")