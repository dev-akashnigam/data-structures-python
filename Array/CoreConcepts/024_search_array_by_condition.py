import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original array, arr = {arr}")

search_result = any(element%4==0 for element in arr)

if search_result:
    print(f"There exists atleast one element in the array which is divisible by 4")

    matching_index_arr = [index for index, element in enumerate(arr) if element%4==0] #array comprehension (filtering + mapping) used.

    first_index = matching_index_arr[0]
    last_index = matching_index_arr[-1]

    print(f"First index in array satisfying the condition, element divisibility by 4 = {first_index}")
    print(f"Last index in array satisfying the condition, element divisibility by 4 = {last_index}")
else:
    print(f"There exists no element in the array which is divisible by 4")