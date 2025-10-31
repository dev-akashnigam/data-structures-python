import array

def fn(element):
    return 100%element==0

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Original Array, arr = {arr}")

filteredArr = array.array('i', filter(fn, arr))
print(f"Filtered Array, filteredArr = {filteredArr}")

