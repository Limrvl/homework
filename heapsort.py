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

def heap_sort(nums):
    length = len(nums)

    for i in range(length, -1, -1):
        heap_extra(nums, length, i)

    for i in range(length - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heap_extra(nums, i, 0)
    return nums

def heap_extra(nums, length, i):
    largest = i
    L = 2 * i + 1
    R = 2 * i + 2

    if L < length and nums[i] < nums[L]:
        largest = L

    if R < length and nums[largest] < nums[R]:
        largest = R

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heap_extra(nums, length, largest)


start_time = datetime.now()
print("Heap sorted array: ", heap_sort(nums))
end_time = datetime.now()
print('---Duration: {}'.format(end_time - start_time))