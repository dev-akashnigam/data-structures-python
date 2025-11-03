import array
from functools import reduce

def fn_sum(element_1, element_2):
    return element_1 + element_2

def fn_mul(element_1, element_2):
    return element_1 * element_2

def fn_max(element_1, element_2):
    if element_1 > element_2:
        return element_1
    else:
        return element_2

arr = array.array('i', [10, 20, 30, 40, 50])

sum_of_all_array_elements = reduce(fn_sum, arr)
print(f"Sum of all array elements = {sum_of_all_array_elements}")

product_of_all_array_elements = reduce(fn_mul, arr)
print(f"Product of all array elements = {product_of_all_array_elements}")

max_of_all_array_elements = reduce(fn_max, arr)
print(f"Max of all array elements = {max_of_all_array_elements}")



