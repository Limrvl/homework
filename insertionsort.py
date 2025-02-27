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

def insertion_sort(nums):
    for i in range(len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and tmp < nums[j]:
            nums[j+1], nums[j] = nums[j], nums[j+1]
            j -= 1
    return nums

start_time = datetime.now()
print("Quick sorted array: ", insertion_sort(nums))
end_time = datetime.now()
print('---Duration: {}'.format(end_time - start_time))