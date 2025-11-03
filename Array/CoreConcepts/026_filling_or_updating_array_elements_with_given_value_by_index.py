import array

arr = array.array('i', [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Original array, arr = {arr}")

value_to_update = 0

arr[:6] = array.array('i', [value_to_update]*(6-0)) # equivalent to arr[0:6] = array.array('i', [value_to_update]*(6-0))
print(f"After filling or updating all array elements from beginning to the 5th index by value: {value_to_update} , arr = {arr}")

value_to_update = 1

arr[6:] = array.array('i', [value_to_update]*(len(arr)-6)) # equivalent to arr[6:len(arr)] = array.array('i', [value_to_update]*(len(arr)-6))
print(f"After filling or updating all array elements from the 6th index to the end by value: {value_to_update} , arr = {arr}")

value_to_update = 2

arr[3:9] = array.array('i', [value_to_update]*(9-3))
print(f"After filling or updating all array elements from the 3rd index to the 8th index by value: {value_to_update} , arr = {arr}")

value_to_update = 3

arr[:] = array.array('i', [value_to_update]*(len(arr)-0)) # equivalent to arr[0:len(arr)] = array.array('i', [value_to_update]*(len(arr)-0))
print(f"After filling or updating all array elements from the beginning to the end by value: {value_to_update} , arr = {arr}")
