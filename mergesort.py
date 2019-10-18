import time
from datetime import datetime
file = open("ai183.txt", "r")
nums = []
test1 = False
test2 = False

while True:
    check = file.read(1)
    if not check:
        break

    if check == "1":
        check = file.read(1)
        if check == "1":
            test1 = True
            check = file.read(1)
            if check == ":":
                test2 = True

    if test1 == True and test2 == True:
        file.seek(file.tell() + 1)
        check = file.read(1)
        while check != "}":
            nums.append(int(check))
            check = file.read(1)
        break

file.close()
print("Array: ", nums)

def merge_sort(nums):
    if len(nums) < 2: return nums

    result, mid = [], int(len(nums) / 2)

    right = merge_sort(nums[mid:])
    left = merge_sort(nums[:mid])

    while (len(left) > 0) and (len(right) > 0):
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    result.extend(left + right)
    return result

start_time = datetime.now()
print("Merge sorted array: ", merge_sort(array))
end_time = datetime.now()
print('---Duration: {}'.format(end_time - start_time))
