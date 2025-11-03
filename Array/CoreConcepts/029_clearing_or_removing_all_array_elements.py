import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original array, arr = {arr}")

del arr[:] #equivalent to arr[0:len(arr)]
print(f"After clearning array, arr = {arr}")