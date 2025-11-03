import array

arr = array.array('i', [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Original array, arr = {arr}")

arrCopyFromBeginningTo5thIndex = arr[:6] # equivalent to arr[0:6]
print(f"Copied array from beginning to 5th index, arrCopyFromBeginningTo5thIndex = {arrCopyFromBeginningTo5thIndex}")

arrCopyFrom5thIndexToEnd = arr[5:] # equivalent to arr[5:len(arr)]
print(f"Copied array from 5th index to end, arrCopyFrom5thIndexToEnd = {arrCopyFrom5thIndexToEnd}")

arrCopyFrom3rdIndexTo8thIndex = arr[3:9]
print(f"Copied array from 3rd index to 8th index, arrCopyFrom3rdIndexTo8thIndex = {arrCopyFrom3rdIndexTo8thIndex}")

fullCopyArr = arr[:] # equivalent to arr[0:len(arr)]
print(f"Full Copy of Array, fullCopyArr = {fullCopyArr}")


