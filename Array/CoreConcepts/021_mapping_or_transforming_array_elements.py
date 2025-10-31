import array

def fn(element):
    return element*element

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original Array, arr = {arr}")

arr = array.array('i', map(fn, arr))
print(f"After mapping/transforming, arr = {arr}")
