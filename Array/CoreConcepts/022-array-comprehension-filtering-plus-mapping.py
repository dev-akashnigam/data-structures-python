# Array Comprehension = Filtering array elements by condition and then transforming/mapping every filtered element.

# syntaxes - 
# [transformation/mappping_expression for element in arr] - no filtering, only mapping/transformation
# [transformation/mappping_expression for element in arr if filter_condition] - filtering + mapping/transformation (IDEAL)
# [transformation/mappping_expression1 if condition else transformation/mappping_expression2 for element in arr] - no filtering, only mapping/transformation by condition.

# "for element in arr" can be replaced with "for index, item in enumerate(arr)" or "for index in range(0, arr.length, 1)"

import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original Array, arr = {arr}")

arr = [element*element for element in arr if 100%element==0]
print(f"After comprehension, arr = {arr}")