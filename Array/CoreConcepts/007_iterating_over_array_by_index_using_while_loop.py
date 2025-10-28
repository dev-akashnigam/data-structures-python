import array

arr = array.array('i', [10, 20, 30, 40, 50])

index = 0
while index < len(arr):
    print(f"arr[{index}] = {arr[index]}")
    index+=1